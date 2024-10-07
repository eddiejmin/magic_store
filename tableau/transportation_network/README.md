# Supply Chain Network Dashboard

### Objective
The purpose of this dashboard is to showcase a typical KPI dashboard for a supply chain network

Magic store is an omnichannel business that sells magical items B2B and B2C. Sales occur in both brick & mortar stores and their own e-commerce webpage.

We want to use the transportation lane and cost data to advice the supply chain executive team how their network is designed and how much it costs to operate. Transportation lanes reflect standard shipping routes among distribution centers, warehouses, and customers. The dashboard focuses on visualizing shipping routes while highlighting inefficiencies due to trucks shipping only one-way. In order to maximize truck utiliziation, shipping lanes will typically aim to load shipments from source to destination and vice versa. Any missing routes represent a cost saving opportunity.

<b>Key Metrics include</b>:
- Total Routes: Number of standard shipping lanes
- Missing Return Lane: Number of shipping lanes without a return shipment route built in
- Average Shipping Cost: Cost to ship from Origin to Destination (Shipping + Warehousing + Fuel)
- Average Shipping Cost (Return): Cost to ship back to Origin utilizing return lane (Shipping + Warehousing + Fuel)


<b>Dimensions</b>
- Origin: Location of shipping warehouse
- Destination: Location of recipient warehouse

<b>Dashboard Highlights</b>
- Utilize 'Actions' to slice dashboard dynamically
- Leverages icons on left-hand side to navigate to Details tab
- Hover over graphs to get precise metric numbers

<b>Resources</b>
- Faux data was created using python. Script can be found in the Magic Store [git](https://github.com/eddiejmin/magic_store/tree/main)
