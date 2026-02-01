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
        
        # Friendly Names for Patients
        readable_names = {k: k.replace('_', ' ').replace('baseline', '').title() for k in feature_cols}
        
        importance_df = pd.DataFrame({
            'Feature': [readable_names.get(f, f) for f in feature_cols],
            'SHAP Value': shap_vals_for_class,
        })
        
        importance_df['Abs_SHAP'] = importance_df['SHAP Value'].abs()
        importance_df = importance_df.sort_values('Abs_SHAP', ascending=False).head(5) # Only show top 5 for simplicity
        
        fig = go.Figure()
        colors = ['#ff6b6b' if x > 0 else '#2ecc71' for x in importance_df['SHAP Value']]
        
        fig.add_trace(go.Bar(
            y=importance_df['Feature'], x=importance_df['SHAP Value'],
            orientation='h', marker=dict(color=colors),
            textposition='none', # Hide numbers for cleaner look
        ))
        
        fig.update_layout(
            title="What influenced this result?",
            xaxis_title="Impact",
            template="plotly_dark", height=300, showlegend=False,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
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
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=hours, y=temp_trend, name='Temp', line=dict(color='#ff6b6b', width=4), mode='lines'))
    fig.add_trace(go.Scatter(x=hours, y=hr_trend, name='Heart Rate', line=dict(color='#4ecdc4', width=4), mode='lines', yaxis='y2'))
    
    fig.update_layout(
        title="Your 24h Trends",
        xaxis=dict(title="Hours ago", showgrid=False),
        yaxis=dict(title=dict(text="Temp (°C)", font=dict(color='#ff6b6b')), showgrid=True, gridcolor='#333'),
        yaxis2=dict(
            title=dict(text="HR (bpm)", font=dict(color='#4ecdc4')),
            anchor='x', overlaying='y', side='right', showgrid=False
        ),
        template="plotly_dark", height=350, hovermode='x unified',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
    )
    
    return fig
