from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

g = Graph()

# This is to set the URL of the RDF file
url = "https://raw.githubusercontent.com/zjyz17/ElectroChemPX/refs/heads/main/electrochem.rdf"

g.parse(url, format="xml")

# Define namespaces (replace with the actual namespaces used in the RDF file)
electrochem = Namespace("http://www.semanticweb.org/zhang/ontologies/2024/12/electrochem#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")


# Query 1: Retrieve reactions with yield of p-toluic acid greater than 50
query1 = prepareQuery('''
    SELECT ?reaction ?yld_value
    WHERE {
      ?reaction electrochem:hasYield ?yld .
      ?yld electrochem:relatesTo electrochem:p_toluic_acid .
      ?yld electrochem:hasNumericalValue ?yld_value .
      FILTER (?yld_value > 50)

    }
''', initNs={"electrochem": electrochem, "rdfs": rdfs})

print("Reaction query results:")
for row in g.query(query1):
    print(f"{row.reaction}, {row.yld_value}")

#
# Query 2: Query the H-cell used for the reactions
query2 = prepareQuery('''
    SELECT ?cell ?anode_material ?cathode_material ?distance_value ?unit
    WHERE {
      ?reaction electrochem:isConductedIn ?cell .
      ?cell electrochem:hasAnode ?anode .
      ?anode  electrochem:isMadeOf ?anode_material.
      ?cell electrochem:hasCathode ?cathode .
      ?cathode  electrochem:isMadeOf ?cathode_material.
      ?cell electrochem:hasElectrodeDistance ?distance .
      ?distance electrochem:hasNumericalValue ?distance_value .
      ?distance electrochem:hasUnitOfMeasure ?unit .
    }
''', initNs={"electrochem": electrochem, "rdfs": rdfs})

print("\nH-cell query results:")
for row in g.query(query2):
    print("Device", row.cell,"Anode material:", row.anode_material, "Cathode material:", row.cathode_material, \
          "Distance:", row.distance_value, row.unit)