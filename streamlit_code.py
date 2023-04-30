import os
import streamlit as st
import glob
import pandas as pd
#from typing_extensions import TypeGuard

st.title("Audio Examples of paper SingIt: A Zero-Shot Many-to-Many Speech to Sing Neural Network")
# st.set_page_config(layout="wide")
st.image('High_level_overview.png')

files_dir = '/sample_audio/sample_audio/full_flow/'

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

col1, col2, col3, col4 = st.columns(4)
with col1:
    #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
    #mix_file = os.path.join(files_dir, 'person_a-original_halleluya-acapella.wav')
    mix_file = 'person_b-m2_s5_speech.wav'
    st.text('output1 signal:')
    st.audio(mix_file)
    #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/person_a-original_halleluya-acapella.wav"

with col2:
    #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
    #mix_file = os.path.join(files_dir, 'person_b-m2_s5_speech.wav')
    mix_file = 'person_b-m2_s5_speech.wav'
    st.text('output2 signal:')
    st.audio(mix_file)
    #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/person_b-m2_s5_speech.wav"

with col3:
    #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
    #mix_file = os.path.join(files_dir, 'output-combined_acapella.wav')
    mix_file = 'person_b-m2_s5_speech.wav'
    st.text('output3 signal:')
    st.audio(mix_file)
    #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/output-combined_acapella.wav"

with col4:
    #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
    #mix_file = os.path.join(files_dir, 'output-combined_with_accompany.wav')
    ix_file = 'person_b-m2_s5_speech.wav'
    st.text('output4 signal:')
    st.audio(mix_file)
    #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/output-combined_with_accompany.wav"

