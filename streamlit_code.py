# import os
# import streamlit as st
# import glob
# #from typing_extensions import TypeGuard
#
# st.title("Audio Examples of paper SingIt: A Zero-Shot Many-to-Many Speech to Sing Neural Network")
# # st.set_page_config(layout="wide")
# st.image('High_level_overview.png')
#
# files_dir = '/sample_audio/sample_audio/full_flow/'
# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
#     #mix_file = os.path.join(files_dir, 'person_a-original_halleluya-acapella.wav')
#     mix_file = 'person_b-m2_s5_speech.wav'
#     st.text('output1 signal:')
#     st.audio(mix_file)
#     #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/person_a-original_halleluya-acapella.wav"
#
# with col2:
#     #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
#     #mix_file = os.path.join(files_dir, 'person_b-m2_s5_speech.wav')
#     mix_file = 'person_b-m2_s5_speech.wav'
#     st.text('output2 signal:')
#     st.audio(mix_file)
#     #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/person_b-m2_s5_speech.wav"
#
# with col3:
#     #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
#     #mix_file = os.path.join(files_dir, 'output-combined_acapella.wav')
#     mix_file = 'person_b-m2_s5_speech.wav'
#     st.text('output3 signal:')
#     st.audio(mix_file)
#     #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/output-combined_acapella.wav"
#
# with col4:
#     #files_dir = '/dsi/gannot-lab/sample_audio/sample_audio/full_flow/'
#     #mix_file = os.path.join(files_dir, 'output-combined_with_accompany.wav')
#     ix_file = 'person_b-m2_s5_speech.wav'
#     st.text('output4 signal:')
#     st.audio(mix_file)
#     #"/dsi/gannot-lab/sample_audio/sample_audio/full_flow/output-combined_with_accompany.wav"
#
""""""""""""""
#
# import streamlit as st
#
# # Set page title and layout
# st.set_page_config(page_title="SingIt! Singer Voice Transformation", layout="wide")
#
# # Add header
# st.title("SingIt! Singer Voice Transformation")
# st.markdown("In this paper, we propose a model which can generate a singing voice from normal speech utterance by harnessing zero-shot, many-to-many style transfer learning. Our goal is to give anyone the opportunity to sing any song in a timely manner. We present a system comprising several available blocks, as well as a modified auto-encoder, and show how this highly-complex challenge can be achieved by tailoring rather simple solutions together. We demonstrate the applicability of the proposed system using a group of 25 non-expert listeners. Samples of the data generated from our model are provided.")
#
# # Add section for Spleeter
# st.header("Spleeter")
# st.markdown("For the vocal separator, we used ‘Spleeter’, a Python package that receives a song (mix of vocals and instruments) as an input and can separate the song into different stems (channels). In our case, we are separating each song into two stems: ‘vocal’ and ‘instrumental’.")
# st.markdown("[Spleeter homepage](https://research.deezer.com/projects/spleeter.html) | [Spleeter GitHub](https://github.com/deezer/spleeter)")
# st.markdown("The new dataset ‘SongList’ was created using the ‘Spleeter’ too.")
# st.write("To each song:")
# st.write("* Original")
# st.write("* Vocal")
# st.write("* Inst’")
#
# # Add section for VCTK
# st.header("VCTK")
# st.markdown("The VCTK corpus includes speech recordings by 109 native English speakers. We use this dataset in inference time as a pool of unseen speakers.")
# st.markdown("[VCTK dataset homepage](https://datashare.ed.ac.uk/handle/10283/2651)")
# st.write("For each:")
# st.write("* Speech only")
#
# # Add section for NHSS
# st.header("NHSS")
# st.markdown("NHSS - a database of parallel recordings of speech and singing. The audio recordings in the NHSS database correspond to a total of 100 songs sung and spoken by 10 singers, 5 male, and 5 female, resulting in a total of 7 hours of audio data.")
# st.markdown("[NHSS paper](https://arxiv.org/abs/2012.00337) | [NHSS database homepage](https://hltnus.github.io/NHSSDatabase/)")
# st.write("For each:")
# st.write("* Speech parallel to song")
#
# # Add section for full flow of the model
# st.header("Full Flow of our Model")
# st.markdown("Each transfer the style of speaker M02 from the NHSS database to a new song from our ‘SongList’ database.")
# st.write("'Person_b-m2_s5_speech.wav' - speech only of M02")
# st.markdown("Add: As noted in the paper, these clips were taken from a parallel dataset in which the speakers also spoke the words of the song. This is irrelevant in our case, and it was treated as regular speech (we anyways used these speech samples for different songs).")
# st.write("'original-Hallelujah' - song mix (vocal +inst’)")
# st.write("'Halleluya-instrumental‘ - inst’ only")
# st.write("'Person_a-original_halleluya-acapella' - original singer vocal only")
# st.write("'Output-combined_acapella' - M02 sings the song - solo")
#
#
# import streamlit as st
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame(
#     np.random.randn(10, 5),
#     columns=('Audio A','Audio B', 'Audio C', 'Audio D'))

# st.table(df)



####################



import streamlit as st

# Set page title and layout
st.set_page_config(page_title="SingIt! Singer Voice Transformation", layout="wide")

# Add header
st.title("SingIt! Singer Voice Transformation")
st.markdown("Abstract: In this paper, we propose a model which can generate a singing voice from normal speech utterance by harnessing zero-shot, many-to-many style transfer learning. Our goal is to give anyone the opportunity to sing any song in a timely manner. We present a system comprising several available blocks, as well as a modified auto-encoder, and show how this highly-complex challenge can be achieved by tailoring rather simple solutions together. We demonstrate the applicability of the proposed system using a group of 25 non-expert listeners. Samples of the data generated from our model are provided.")


st.header('SingIt Style Transfer Examples')

# Song 1
st.subheader('Song 1 - Hallelujah')

cols = st.columns(5)
cols[1].write("Segment A")
cols[2].write("Segment B")
cols[3].write("Segment C")
cols[4].write("Segment D")

row_names = ["(1) Person B - speech", "(2) Original song", "(3) Instrumental solo","(4) Vocal solo","(5) SingIt transfer"]
for i in range(5): # number of rows in your table! = 2
    cols = st.columns(5) # number of columns in each row! = 2
    # first column of the ith row
    cols[0].write(row_names[i])
    cols[1].audio("person_b-m2_s5_speech.wav")
    cols[2].audio("person_b-m2_s5_speech.wav")
    cols[3].audio("person_b-m2_s5_speech.wav")
    cols[4].audio("person_b-m2_s5_speech.wav")

# Song 2
st.subheader('Song 2 - Hey Jude')

cols = st.columns(5)
cols[1].write("Segment A")
cols[2].write("Segment B")
cols[3].write("Segment C")
cols[4].write("Segment D")

row_names = ["(1) Person B - speech", "(2) Original song", "(3) Instrumental solo","(4) Vocal solo","(5) SingIt transfer"]
for i in range(5): # number of rows in your table! = 2
    cols = st.columns(5) # number of columns in each row! = 2
    # first column of the ith row
    cols[0].write(row_names[i])
    cols[1].audio("person_b-m2_s5_speech.wav")
    cols[2].audio("person_b-m2_s5_speech.wav")
    cols[3].audio("person_b-m2_s5_speech.wav")
    cols[4].audio("person_b-m2_s5_speech.wav")

# Song 3
st.subheader('Song 3 - Billie Jean')

cols = st.columns(5)
cols[1].write("Segment A")
cols[2].write("Segment B")
cols[3].write("Segment C")
cols[4].write("Segment D")

row_names = ["(1) Person B - speech", "(4) Vocal solo","(5) SingIt transfer"]
for i in range(3): # number of rows in your table! = 2
    cols = st.columns(5) # number of columns in each row! = 2
    # first column of the ith row
    cols[0].write(row_names[i])
    cols[1].audio("person_b-m2_s5_speech.wav")
    cols[2].audio("person_b-m2_s5_speech.wav")
    cols[3].audio("person_b-m2_s5_speech.wav")
    cols[4].audio("person_b-m2_s5_speech.wav")
