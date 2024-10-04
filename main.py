from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

# 数据准备
labels = ['普通门诊', '特需门诊', '专家门诊']
values = [30, 30, 40]
colors = ['#e74c3c', '#2ecc71', '#f1c40f']

# 创建DataFrame
df = pd.DataFrame(dict(类别=labels, 数值=values))

# 使用Plotly绘制饼图
fig = px.pie(df, values='数值', names='类别', color_discrete_sequence=colors,
             title='门诊类型分布')


@app.route('/')
def index():
    # 将饼图转换为HTML格式以便在模板中使用
    graphJSON = fig.to_json()

    return render_template('index.html', graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(debug=True)