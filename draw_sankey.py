# -*- coding: utf-8 -*-
# @Author  : ifan
# @FileName: draw_sankey.py
# @Time    : 2024/3/22 15:24
import pandas
from pyecharts.charts import Sankey
from pyecharts import options as opts
data = pandas.read_excel("demo.xlsx", sheet_name='Sheet1')

# 设置节点属性

nodes = [
    {"name": "低密度耕地",
     "itemStyle": {"color": "#FFFFAF","borderColor": "#FFFFAF" },
    },
    {"name": "低密度耕地1",
     "itemStyle": { "color": "#FFFFAF", "borderColor": "#FFFFAF"},
    },
    {"name": "中密度耕地",
     "itemStyle": { "color": "#FFD37F", "borderColor": "#FFD37F"},
    },
    {"name": "中密度耕地1",
     "itemStyle": { "color": "#FFD37F", "borderColor": "#FFD37F"},
    },
    {"name": "高密度耕地",
     "itemStyle": { "color": "#FFAA00", "borderColor": "#FFAA00"},
    },
    {"name": "高密度耕地1",
     "itemStyle": { "color": "#FFAA00", "borderColor": "#FFAA00"},
    },

    {"name": "低密度林地",
     "itemStyle": { "color": "#98E600", "borderColor": "#98E600"},
    },
    {"name": "低密度林地1",
     "itemStyle": { "color": "#98E600", "borderColor": "#98E600"},
    },

    {"name": "中密度林地",
     "itemStyle": { "color": "#70A800", "borderColor": "#70A800"},
    },
    {"name": "中密度林地1",
     "itemStyle": { "color": "#70A800", "borderColor": "#70A800"},
    },
    {"name": "高密度林地",
     "itemStyle": { "color": "#4C7300", "borderColor": "#4C7300"},
    },
    {"name": "高密度林地1",
     "itemStyle": { "color": "#4C7300", "borderColor": "#4C7300"},
    },
    {"name": "低密度草地",
     "itemStyle": { "color": "#E9FFBE", "borderColor": "#E9FFBE"},
    },
    {"name": "低密度草地1",
     "itemStyle": { "color": "#E9FFBE", "borderColor": "#E9FFBE"},
    },

    {"name": "中密度草地",
     "itemStyle": { "color": "#D1FF73", "borderColor": "#D1FF73"},
    },
    {"name": "中密度草地1",
     "itemStyle": { "color": "#D1FF73", "borderColor": "#D1FF73"},
    },
    {"name": "高密度草地",
     "itemStyle": { "color": "#91cc75", "borderColor": "#91cc75"},
    },
    {"name": "高密度草地1",
     "itemStyle": { "color": "#AAFF00", "borderColor": "#AAFF00"}
    },
    {"name": "低密度灌木",
     "itemStyle": { "color": "#E6E600", "borderColor": "#E6E600"},
    },
    {"name": "低密度灌木1",
     "itemStyle": { "color": "#E6E600", "borderColor": "#E6E600"},
    },
    {"name": "中密度灌木",
     "itemStyle": { "color": "#A8A800", "borderColor": "#A8A800"},
    },
    {"name": "中密度灌木1",
     "itemStyle": { "color": "#A8A800", "borderColor": "#A8A800"},
    },
    {"name": "高密度灌木",
     "itemStyle": { "color": "#737300", "borderColor": "#737300"},
    },
    {"name": "高密度灌木1",
     "itemStyle": { "color": "#737300", "borderColor": "#737300"},
    },
    {"name": "低密度湿地",
     "itemStyle": { "color": "#E8BEFF", "borderColor": "#E8BEFF"},
    },
    {"name": "低密度湿地1",
     "itemStyle": { "color": "#E8BEFF", "borderColor": "#E8BEFF"},
    },
    
    {"name": "中密度湿地",
    "itemStyle": { "color": "#DF73FF", "borderColor": "#DF73FF"},
    },

    {"name": "中密度湿地1",
     "itemStyle": { "color": "#DF73FF", "borderColor": "#DF73FF"},
    },

    {"name": "高密度湿地",
     "itemStyle": { "color": "#C500FF", "borderColor": "#C500FF"},
    },

    {"name": "高密度湿地1",
     "itemStyle": { "color": "#C500FF", "borderColor": "#C500FF"},
    },

    {"name": "低密度水体",
     "itemStyle": { "color": "#BED2FF", "borderColor": "#BED2FF"},
    },
    {"name": "低密度水体1",
     "itemStyle": { "color": "#BED2FF", "borderColor": "#BED2FF"},
    },
    {"name": "中密度水体",
     "itemStyle": { "color": "#73B2FF", "borderColor": "#73B2FF"},
    },
    {"name": "中密度水体1",
     "itemStyle": { "color": "#73B2FF", "borderColor": "#73B2FF"},
    },
    {"name": "高密度水体",
     "itemStyle": { "color": "#0070FF", "borderColor": "#0070FF"},
    },
    {"name": "高密度水体1",
     "itemStyle": { "color": "#0070FF", "borderColor": "#0070FF"},
    },
    {"name": "低密度建设用地",
     "itemStyle": { "color": "#FF7F7F", "borderColor": "#FF7F7F"},
    },
    {"name": "低密度建设用地1",
     "itemStyle": { "color": "#FF7F7F", "borderColor": "#FF7F7F"},
    },
    {"name": "中密度建设用地",
     "itemStyle": { "color": "#A80000", "borderColor": "#A80000"},
    },
    {"name": "中密度建设用地1",
     "itemStyle": { "color": "#A80000", "borderColor": "#A80000"},
    },
    {"name": "高密度建设用地",
     "itemStyle": { "color": "#730000", "borderColor": "#730000"},
    },
    {"name": "高密度建设用地1",
     "itemStyle": { "color": "#730000", "borderColor": "#730000"},
    },
    {"name": "低密度裸地",
     "itemStyle": { "color": "#E1E1E1", "borderColor": "#E1E1E1"},
    },
    {"name": "低密度裸地1",
     "itemStyle": { "color": "#E1E1E1", "borderColor": "#E1E1E1"},
    },
    {"name": "中密度裸地",
     "itemStyle": { "color": "#CCCCCC", "borderColor": "#CCCCCC"},
    },
    {"name": "中密度裸地1",
     "itemStyle": { "color": "#CCCCCC", "borderColor": "#CCCCCC"},
    },
    {"name": "高密度裸地",
     "itemStyle": { "color": "#9C9C9C", "borderColor": "#9C9C9C"},
    },

    {"name": "高密度裸地1",
     "itemStyle": { "color": "#9C9C9C", "borderColor": "#9C9C9C"},
    },
]

#print(nodes[0]['itemStyle']['color'])

links = []
for x, y, z in zip(data.Source, data.Target, data.Value):
    d2 = {}
    d2['source'] = x
    d2['target'] = y
    d2['value'] = z

    for k in range(0,len(nodes)):
        if nodes[k]['name'] == x:
            color1 = nodes[k]['itemStyle']['color']
        if nodes[k]['name'] == y:
            color2 = nodes[k]['itemStyle']['color']

    d2["lineStyle"] = {"color": {
                "type": "linear",
        "x": 0,
        "y": 0,
        "x2": 1,
        "y2": 1,
        "colorStops": [{"offset": 0,"color": color1}, 
                    {"offset": 1,"color": color2}]
        }}
    
    links.append(d2)

    #print(links)



pic = (
    Sankey(init_opts=opts.InitOpts(width="700px", height="900px")).add("Land class",  # Lengend name
                                                                        nodes,  # nodes
                                                                        links,  # links
                                                                        # 设置透明度、弯曲度、颜色
                                                                        linestyle_opt = opts.LineStyleOpts(opacity=0.5,
                                                                                                         curve = 0.5,
                                                                                                         ),
                                                                        
                                                                        label_opts = opts.LabelOpts(
                                                                            position="outside",
                                                                            is_show = False,
                                                                            ),

                                                                        # position options: 'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight'...
                                                                        # is_show options： Ture , False

                                                                        node_gap = 10,  # 节点之前的距离
                                                                        layout_iterations = 0, # 默认数值是32，当设置为0的时候，节点的显示按照出现顺序
                                                                        
                                                                        # orient="vertical"  # 垂直显示
                                                                        ).set_global_opts(
       title_opts = opts.TitleOpts(title="Sankey_demo"))
)
pic.render("LandClass_ZYIB.html")



