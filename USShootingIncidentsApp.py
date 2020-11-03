import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly
import plotly.graph_objects as go
import pandas as pd


keys = []
values = []
for i in range(1984, 2017):
    keys.append(str(i))
    values.append(i)

dropdown = dict(zip(keys, values))

external_css = [dbc.themes.BOOTSTRAP, '/static/reset.css']
external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']


app = dash.Dash(
    "idk",
    external_stylesheets=external_css,
    external_scripts=external_js
)


app.layout = html.Div([
    dbc.Jumbotron([
        html.H1("US Shooting Incidents 1984-2016", className="display-3", style={"textAlign": "center"}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row([
            dbc.Input(id="dropdown_time", type="number", value=1984, max=2016, min=1984, step=1,
                      style={'width': '1204px', 'fontSize': '22px'}),
            dbc.Button("Submit", id="submit", style={'width': '150px', 'fontSize': '22px'}),
        ], justify="center", align="center", className="h-50"),

        dbc.Tooltip(
            "Click to load new data.",
            target="submit",
        ),

        html.Br(),
        dbc.Spinner(html.Div(id="loading-output"), spinner_style={"width": "3rem", "height": "3rem"}),
        html.Br(),
        html.Br(),
        dbc.Row([
            html.H1("Number of incidents per day in", className="display-3",
                style={"fontSize": "55px", "margin-left": "12px"}),
            html.Div(id="year_output", className="display-3", style={"fontSize": "55px", "margin-left": "12px"})
        ]),

        html.Br(),
        dcc.Graph(id="number_graph"),
        html.Br(),
        html.H1("Types of incidents per day", className="display-3",
                style={"fontSize": "55px"}),
        html.Br(),
        dcc.Graph(id="type_graph"),
        html.Br(),
        html.Br(),
        html.H1("Most of deaths are caused by gun-related violence", className="display-3",
                style={"fontSize": "55px"}),
        html.Br(),
        dbc.Row([
            dcc.Graph(id="pie_chart", style={"height": "40%", "width": "50%", "margin-left": "16px",
                                                                              "margin-top": "15px"}),
            dbc.Col([
                html.H3("Gun violence statistics", className="display-3", style={"margin-left": "5px",
                    "fontSize": "45px"}),
                html.Br(),
                html.P("How many people die from gun-related violence worldwide?", className="lead",
                       style={"margin-left": "11px", "fontSize": "23px"}),
                html.Ul([
                    html.Li("More than 500 people die every day from gun violence"),
                    html.Li("44% of all homicides globally involve gun violence"),
                    html.Li("There were 1.4 million firearm-related deaths globally between 2012 and 2016"),
                ], className="lead", style={"fontSize": "23px"}),
                html.P("The majority of victims and perpetrators are young men, but women are particularly at risk of"
                       " firearms violence perpetrated by an intimate partner. Sexual violence can also"
                       " be facilitated by firearms.", className="lead", style={"margin-left": "11px",
                                                                                "fontSize": "23px"}
                       ),
            ])
        ]),
        html.Br(),
        html.H3("How many people are injured by gunshots worldwide?", className="display-3",
                style={"fontSize": "45px"}),
        html.Br(),
        html.Ul([
            html.Li("An estimated 2,000 people are injured by gunshots every single day"),
            html.Li("At least 2 million people are living with firearm injuries around the globe"),
        ], className="lead", style={"fontSize": "23px"}),
        html.P("Millions of people suffer the severe and long-term psychological effects that gun violence "
               "– or the threat of gun violence – brings to individuals, families and their wider community.",
               className="lead", style={"fontSize": "23px"}),
        html.Br(),
        html.P("In the USA, nearly 134,000 people were shot and injured by firearms in 2017.", className="lead",
               style={"fontSize": "23px"}),
        html.Br(),
        html.P("Gunshot injuries are often life-changing and have an indelible impact on the victims’ long-term mental"
               " and physical health. Some need permanent, lifelong care, and many others lose their ability to work,"
               " particularly in physically demanding jobs. Yet programmes offering adequate long-term care,"
               " rehabilitation and job retraining are virtually non-existent. The toll that gun violence has "
               "on victims, family members and the medical services has resulted in a chronic public health crisis "
               "– with remarkably little government response. Access to affordable and quality health care services "
               "in the USA should include necessary long-term health interventions, including long-term pain"
               " management, rehabilitation and other support services, and mental health care.",
               className="lead", style={"fontSize": "23px"}),
        html.Br(),
        html.H3("How many guns are produced every year globally?", className="display-3", style={"fontSize": "55px",
                "margin-right": "10px"}),
        html.Br(),
        html.P("There are 8 million new small arms and up to 15 billion rounds of ammunition produced each year.",
               className="lead", style={"fontSize": "23px"}),
        html.Br(),

        html.P("Source: ", className="lead"),
        html.Ul([
            html.Li(html.A("https://www.amnesty.org/en/what-we-do/arms-control/gun-violence/",
                href="https://www.amnesty.org/en/what-we-do/arms-control/gun-violence/", target="_blank")),
            html.Li(html.A("https://github.com/plotly/datasets/blob/master/US-shooting-incidents.csv",
                href="https://www.amnesty.org/en/what-we-do/arms-control/gun-violence/", target="_blank")),
        ]),
        html.Br(),
        html.Hr(),
        dbc.Row([
            dbc.Col(),
            dbc.Col([
                html.P("Contact me: piotr.blaszczak2002@gmail.com", className="lead", style={"textAlign": "center",
                                                                                             "margin-top": "25px"})
            ]),
            dbc.Col(
                html.Div([
                    html.A([
                        html.Img(src="https://icons-for-free.com/"
                                     "iconfiles/png/512/fb+logo+social+icon-1320191784031142975.png",
                                 style={"width": "80px"})
                    ], href="https://www.facebook.com/piotrekstrzelec.town"),
                    html.A([
                        html.Img(src="static/instagram.png",
                                 style={"width": "70px"})
                    ], href="https://www.facebook.com/piotrekstrzelec.town"),
                    html.A([
                        html.Img(src="static/twitter.png",
                                 style={"width": "70px", "height": "80px", "margin-left": "5px"})
                    ], href="https://twitter.com/Juan65594084"),


                ], style={"margin-left": "205px", "textAlign": "right"})
            )
        ]),
        html.Hr(),
        html.H3([
            html.Strong("© 2020 Copyright: Piotr Błaszczak", style={"fontSize": "20px"})
        ], style={"textAlign": "center", "margin-top": "55px"})
    ], style={"margin-left": "50px", "margin-right": "50px", "background": "#d9d9d9"})


], style={"background": "#393d3f"})


@app.callback(
    [Output("loading-output", "children"),
     Output("number_graph", "figure"),
     Output("type_graph", "figure"),
     Output("pie_chart", "figure"),
     Output("year_output", "children")],
    [Input("submit", "n_clicks")],
    [State("dropdown_time", "value")]
)
def update(n, value):
    if value is None:
        raise PreventUpdate
    else:

        data = pd.read_csv("US-shooting-incidents.csv")
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            unique_values = data["cause_short"].unique()
            labels = []
            values = []
            year = data.loc[data['year'] == int(value)]

            for label in unique_values:
                if len(year['cause_short'].loc[year['cause_short'] == label].to_list()) > 0:
                    values.append(len(year['cause_short'].loc[year['cause_short'] == label].to_list()))
                    labels.append(label)

            number_of_incidents = []
            dates = []

            for i in year['date']:
                number_of_incidents.append(len(year.loc[year['date'] == i]))
                dates.append(i)

            dates = list(set(year['date'].to_list()))
            dates.sort()
            number_of_incidents = []
            for date in dates:
                number_of_incidents.append(len(year.loc[year['date'] == date]))

            x = dates
            y = number_of_incidents

            data = plotly.graph_objects.Bar(
                x=x,
                xaxis="x",
                y=y,
                yaxis="y",
                name='MainGraph',
            )

            number_graph = {"data": [data], "layout": go.Layout(
                xaxis=dict(title="Date", side="left"),
                yaxis=dict(title="Number of incidents", side="left"),
                plot_bgcolor="#bfc0c0",
                paper_bgcolor="#bfc0c0",
            )}

            x = year['date']
            y = year['cause_short']

            data = plotly.graph_objects.Scatter(
                x=x,
                xaxis="x",
                y=y,
                yaxis="y",
                name='MainGraph',
                mode="markers"
            )

            type_graph = {"data": [data], "layout": go.Layout(
                xaxis=dict(title="Date", side="left"),
                yaxis=dict(side="left", tickangle=50),
                plot_bgcolor="#bfc0c0",
                paper_bgcolor="#bfc0c0",
            )}

            pie_data = go.Pie(
                labels=labels,
                values=values,
                name='PieChart'
            )

            data = [pie_data]

            layout = go.Layout(
                title="Percentage of types of incidents",
                plot_bgcolor="#bfc0c0",
                paper_bgcolor="#bfc0c0",
            )

            pie = go.Figure(data=data, layout=layout)

            return "", number_graph, type_graph, pie, value


if __name__ == '__main__':
    app.run_server(debug=True)
