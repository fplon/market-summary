# https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946

from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

import yfinance_sample as yfs

app = Flask(__name__, template_folder="templates")


@app.route("/")
def notdash():
    perf_table = yfs.create_perf_table()
    fig = yfs.create_perf_table_chart(perf_table=perf_table, chart_type="plotly_bar")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("notdash.html", graphJSON=graphJSON)


# python -m flask run
if __name__ == "__main__":
    app.run()
