# plots.py
import plotly.graph_objects as go
import pandas as pd
import shap

def plot_shap_analysis(base_model, input_row, pred_class, feature_cols):
    try:
        explainer = shap.TreeExplainer(base_model)
        shap_values = explainer.shap_values(input_row)
        
        if isinstance(shap_values, list):
            shap_vals_for_class = shap_values[pred_class][0]
        else:
            shap_vals_for_class = shap_values[0]
        
        # أسماء مختصرة للجوال
        readable_names = {k: k.split('_')[1].upper() if len(k.split('_')) > 1 else k for k in feature_cols}
        
        importance_df = pd.DataFrame({
            'Feature': [readable_names.get(f, f) for f in feature_cols],
            'SHAP Value': shap_vals_for_class,
        })
        
        importance_df['Abs_SHAP'] = importance_df['SHAP Value'].abs()
        importance_df = importance_df.sort_values('Abs_SHAP', ascending=False).head(5) # أفضل 5 فقط للجوال
        
        fig = go.Figure()
        colors = ['#ff6b6b' if x > 0 else '#2ecc71' for x in importance_df['SHAP Value']]
        
        fig.add_trace(go.Bar(
            y=importance_df['Feature'], x=importance_df['SHAP Value'],
            orientation='h', marker=dict(color=colors, borderRadius=5),
            textposition='none'
        ))
        
        fig.update_layout(
            title=dict(text="Top Influencing Factors", font=dict(size=14, color='white')),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(tickfont=dict(color='white')),
            margin=dict(l=10, r=10, t=30, b=10),
            height=200,
            showlegend=False
        )
        return fig, importance_df
    except Exception as e:
        return None, str(e)

def plot_vital_trends(baseline_data, last_data, risk_class):
    hours = [0, 6, 12, 18, 24]
    
    # دالة بسيطة لإنشاء بيانات وهمية للرسم (Trend)
    def get_trend(base, last):
        return [base] + [base + (last - base) * (i/24) for i in [6,12,18]] + [last]

    temp_trend = get_trend(baseline_data['temp'], last_data['temp'])
    hr_trend = get_trend(baseline_data['hr'], last_data['hr'])
    
    fig = go.Figure()
    
    # الحرارة
    fig.add_trace(go.Scatter(x=hours, y=temp_trend, name='Temp', 
                            line=dict(color='#ff6b6b', width=3, shape='spline')))
    
    # النبض
    fig.add_trace(go.Scatter(x=hours, y=hr_trend, name='HR', 
                            line=dict(color='#4ecdc4', width=3, shape='spline'), yaxis='y2'))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=30, b=10),
        height=200,
        showlegend=False,
        title=dict(text="24h Trend", font=dict(size=14, color='white')),
        xaxis=dict(showgrid=False, tickfont=dict(color='gray')),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', tickfont=dict(color='#ff6b6b')),
        yaxis2=dict(anchor='x', overlaying='y', side='right', showgrid=False, tickfont=dict(color='#4ecdc4'))
    )
    
    return fig
