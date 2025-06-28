import numpy as np
from .problem import Problem
from scipy.integrate import solve_ivp
import autograd.numpy as anp


class Reaction_categ(Problem):

    def __init__(self):
        super().__init__(n_var=8, n_obj=2, n_constr=0, xl=np.array([1,0.1,0,0,0,0,0,0]), xu=np.array([1.5,6,1,1,1,1,1,1]))


    def _evaluate(self, x, out, *args, requires_F=True, **kwargs):

        if requires_F:

            sty_res = []
            e_fac_res = []

            for i in range(0, len(x)):

                equiv = x[i][0]
                flowrate = x[i][1]

                solv_index = np.argmax(x[i][2:6])
                solv_code = np.zeros_like(x[i][2:6])
                solv_code[solv_index] = 1

                if solv_index == 0:
                    solv = "THF"
                elif solv_index == 1:
                    solv = "EtOAc"
                elif solv_index == 2:
                    solv = "MeCN"
                elif solv_index == 3:
                    solv = "Toluene"

                elec_index = np.argmax(x[i][6:8])
                elec_code = np.zeros_like(x[i][6:8])
                elec_code[elec_index] = 1

                if elec_index == 1:
                    elec = "Acetic_anhydride"
                elif elec_index == 0:
                    elec = "Acetyl_chloride"

                v = 2e-3 * flowrate / 60
                c0 = np.array([equiv * 0.30, 0.30, 0, 0])

                if elec == "Acetic_anhydride":
                    k0 = np.array([40, 0.2])
                else:
                    k0 = np.array([30, 0.3])

                if solv == "Toluene":
                    phi = 0.35
                    k0[0] = 25
                elif solv == "EtOAc":
                    phi = 0.35
                    k0[0] = 60
                elif solv == "MeCN":
                    if elec == "Acetic_anhydride":
                        phi = 0.09 * flowrate + 0.02
                        k0[0] = 40
                    else:
                        phi = 0.04 * flowrate + 0.1
                        k0[0] = 40
                elif solv == "THF":
                    if elec == "Acetic_anhydride":
                        phi = 0.19 * flowrate - 0.11
                        k0[0] = 40
                    else:
                        phi = 0.05 * flowrate + 0.06
                        k0[0] = 40
                else:
                    raise ValueError(f"Unknown solvent: {solv}")


                def calculate(c0, k0, phi, v):
                    # Parameters
                    Nu = np.array([[-1, -1], [-1, 0], [1, 0], [0, 1]])  # Reaction stoichimetry
                    Vr = 0.5 * 1e-3  # Reactor volume, L
                    Nocomp = 4
                    Noreac = 2
                    order = np.array([[1, 1], [1, 0], [0, 0], [0, 0]])  # Reaction order

                    def f(tau, c):
                        dcdtau = np.zeros(Nocomp)
                        Rate = np.zeros(Noreac)

                        for i in range(0, Noreac):
                            Rate[i] = k0[i] * np.prod((c * phi) ** order[:, i])  # mixing index phi

                        for i in range(0, Nocomp):
                            dcdtau[i] = np.sum(Rate * Nu[i, :])

                        return np.array(dcdtau)

                    # Integrate
                    tau_span = np.array([0, Vr / v])
                    spaces = np.linspace(tau_span[0], tau_span[1], 100)
                    soln = solve_ivp(f, tau_span, c0, t_eval=spaces)

                    # Results
                    tau = soln.t
                    cA = soln.y[0]
                    cB = soln.y[1]
                    cC = soln.y[2]
                    cD = soln.y[3]

                    return tau, cA, cB, cC, cD

                tau, cA, cB, cC, cD = calculate(c0, k0, phi, v)
                yield_pred = round(100 * (cC[-1]) / 0.3, 2)

                # calculate STY and E_factor
                Mw_product = 149.19
                Mw_anhyride = 102.09
                Mw_chloride = 78.5
                Mw_NaOH = 40

                res_time = 0.5 / (flowrate * 2 / 60)
                STY = 0.3 * Mw_product * (yield_pred / 100) / (0.5 * res_time) / 4  # realise later

                if elec == "Acetic_anhydride":
                    waste = (
                            107.15
                            + equiv * (Mw_anhyride + Mw_NaOH)
                            - Mw_product * (yield_pred / 100)
                    )
                else:
                    waste = (
                            107.15
                            + equiv * (Mw_chloride + Mw_NaOH)
                            - Mw_product * (yield_pred / 100)
                    )

                E_factor = waste / (Mw_product * (yield_pred / 100))

                sty_res.append(-STY) # assume min in the algorithm
                e_fac_res.append(E_factor)

            out["F"] = anp.column_stack([sty_res, e_fac_res])