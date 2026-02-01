# plots.py
import plotly.graph_objects as go
import pandas as pd
import shap
import streamlit as st

def plot_shap_analysis(base_model, input_row, pred_class, feature_cols):
    try:
        explainer = shap.TreeExplainer(base_model)
        shap_values = explainer.shap_values(input_row)
        
        if isinstance(shap_values, list):
            shap_vals_for_class = shap_values[pred_class][0]
        else:
            shap_vals_for_class = shap_values[0]
        
        readable_names = {k: k.replace('_', ' ').title() for k in feature_cols}
        
        importance_df = pd.DataFrame({
            'Feature': [readable_names.get(f, f) for f in feature_cols],
            'SHAP Value': shap_vals_for_class,
        })
        
        importance_df['Abs_SHAP'] = importance_df['SHAP Value'].abs()
        importance_df = importance_df.sort_values('Abs_SHAP', ascending=False).head(8)
        
        fig = go.Figure()
        colors = ['#ff6b6b' if x > 0 else '#2ecc71' for x in importance_df['SHAP Value']]
        
        fig.add_trace(go.Bar(
            y=importance_df['Feature'], x=importance_df['SHAP Value'],
            orientation='h', marker=dict(color=colors),
            text=[f"{val:.3f}" for val in importance_df['SHAP Value']],
            textposition='outside',
        ))
        
        fig.update_layout(
            title="Key Factors Influencing AI Decision",
            xaxis_title="Impact (SHAP Value)",
            template="plotly_dark", height=400, showlegend=False,
            margin=dict(l=200)
        )
        return fig, importance_df
    except Exception as e:
        return None, str(e)

def plot_vital_trends(baseline_data, last_data, risk_class):
    hours = [0, 6, 12, 18, 24]
    
    def get_trend(base, last):
        return [base] + [base + (last - base) * (i/24) for i in [6,12,18]] + [last]

    temp_trend = get_trend(baseline_data['temp'], last_data['temp'])
    hr_trend = get_trend(baseline_data['hr'], last_data['hr'])
    rr_trend = get_trend(baseline_data['rr'], last_data['rr'])
    spo2_trend = get_trend(baseline_data['spo2'], last_data['spo2'])

    fig = go.Figure()
    
    # Temp
    fig.add_trace(go.Scatter(x=hours, y=temp_trend, name='Temp (°C)', line=dict(color='#ff6b6b', width=3), mode='lines+markers'))
    
    # Heart Rate (Right Axis)
    fig.add_trace(go.Scatter(x=hours, y=hr_trend, name='HR (bpm)', line=dict(color='#4ecdc4', width=3), mode='lines+markers', yaxis='y2'))
    
    fig.update_layout(
        title="24h Vital Signs Trends",
        xaxis=dict(title="Time (hours)"),
        yaxis=dict(title="Temperature (°C)", titlefont=dict(color='#ff6b6b')),
        yaxis2=dict(title="Heart Rate (bpm)", titlefont=dict(color='#4ecdc4'), anchor='x', overlaying='y', side='right'),
        template="plotly_dark", height=450, hovermode='x unified',
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
    )
    
    if risk_class == 2:
        fig.add_hrect(y0=37.5, y1=42, fillcolor="red", opacity=0.1, layer="below", annotation_text="Fever Zone")

    return fig
