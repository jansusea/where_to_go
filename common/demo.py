from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))\
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])\
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])\
    .set_global_opts(title_opts=opts.TitleOpts(title="主编同",
                                               subtitle="副标题"))\
    .render()
