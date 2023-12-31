import datetime as dt
import plotly.graph_objects as go


class CandlePlot:

    def __init__(self, df):
        self.df_plot = df.copy()
        self.create_candle_fig()

    def add_time_str(self):
        self.df_plot['sTime'] = [dt.datetime.strftime(x,
                                                      "s%y-%m-%d %H:%M") for x in self.df_plot.time]

    def create_candle_fig(self):
        self.add_time_str()
        self.fig = go.Figure()
        self.fig.add_trace(go.Candlestick(
            x=self.df_plot.sTime,
            open=self.df_plot.mid_o,
            high=self.df_plot.mid_h,
            low=self.df_plot.mid_l,
            close=self.df_plot.mid_c,
            line=dict(width=1), opacity=1,
            increasing_fillcolor='#24A06B',
            decreasing_fillcolor='#CC2E3C',
            increasing_line_color='#2EC886',
            decreasing_line_color='#FF3A4C'
        ))

    def update_layout(self, width, height, nticks):
        self.fig.update_yaxes(
            gridcolor='#1F292F'
        )

        self.fig.update_xaxes(
            gridcolor='#1F292F',
            rangeslider=dict(visible=False),
            nticks=nticks
        )

        self.fig.update_layout(
            width=width,
            height=height,
            margin=dict(l=10, r=10, b=10, t=10),
            paper_bgcolor='#2C303C',
            plot_bgcolor='#2C303C',
            font=dict(size=8, color='#E1E1E1')
        )

    # * Calling the Update_layout function here
    def show_plot(self, width=900, height=400, nticks=5):
        self.update_layout(width, height, nticks)
        self.fig.show()
