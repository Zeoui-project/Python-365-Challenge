# %% [markdown]
# # Plotly Graph using Python

# %%
%pip install plotly

# %%
import plotly.express as plotly
import plotly.graph_objects as graph

# %%
# Draw bar Chart
plot = plotly.bar(x=['D1', 'D2', 'D3'], y=[1, 2, 3])
plot.show()

# %%
# Draw Scatter Chart
plot = plotly.scatter(x=[1, 2, 3], y=[1, 2, 3])
plot.show()

# %%
# Draw Pie Chart
plot = plotly.pie(labels=['D1', 'D2', 'D3',], values=[1, 2, 3])
plot.show()

# %%
# Draw Histogram
plot = plotly.histogram(x=[1, 2, 3])
plot.show()

# %%
# Draw Box Plot
plot = plotly.box(x=[1, 2, 3])
plot.show()

# %%
# Draw Finnance Candlestick Chart
plot = graph.Figure(data=[graph.Candlestick(x=[1, 2, 3], open=[1, 2, 3], high=[1, 2, 3], low=[1, 2, 3], close=[1, 2, 4])])
plot.show()s