#! python3
# Project002_OneCare.py

"""
This script pulls financials from delimited text files to 
create a Sankey Diagram.
"""

import pandas, plotly.offline as py

# Transform & Load into Database
def load_data():
    nodes = pandas.read_table('Project002_Data_Sankey_Revenue_Nodes.txt', sep='|')
    links = pandas.read_table('Project002_Data_Sankey_Revenue_Links.txt', sep='|')

    links["Dollars"] = links["Dollars"].astype(float)

    links["Source"] = links["Source"].astype(int)
    links["Target"] = links["Target"].astype(int)
    
#    print(nodes["Label"].tolist())
#    print(links["Source"].tolist())
#    print(links["Target"].tolist())
#    print(links["2017"].tolist())


    data = dict(
    type='sankey',
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(
        color = "black",
        width = 2.5),
      label = nodes["Label"],
      color = nodes["Color"]),
    link = dict(
      source = links["Source"],
      target = links["Target"],
      value = links["Dollars"],
      color = links["Color"]))

    layout =  dict(
            title = "All Payer Money Flow",
            font = dict(
            size = 20))

    fig = dict(data=[data], layout=layout)
    py.plot(fig, validate=False)

load_data()