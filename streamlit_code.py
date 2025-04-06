import streamlit as st
st.set_page_config(page_title="SingIt! Singer Voice Transformation", layout="centered")
st.title("SingIt! Singer Voice Transformation")

col1, col2 = st.columns([5, 4])
col1.markdown("**Abstract:** In this paper, we propose a model which can generate a singing voice from normal speech utterance by harnessing zero-shot, many-to-many style transfer learning. Our goal is to give anyone the opportunity to sing any song in a timely manner. We present a system comprising several available blocks, as well as a modified auto-encoder, and show how this highly-complex challenge can be achieved by tailoring rather simple solutions together. We demonstrate the applicability of the proposed system using a group of 25 non-expert listeners. Samples of the data generated from our model are provided.")
col2.write(" \n")
st.write("Our [Paper](https://arxiv.org/abs/2405.04627/) (arxiv):.")
col2.write(" \n")
col2.write(" \n")
col2.write(" \n")
col2.image("figures/High_level_overview.png", caption="High level system overview")

st.markdown("""---""")

# Section 1 - SingIt Transfer
st.header('SingIt Style Transfer Examples')

col1, col2, col3 = st.columns([1, 5, 1])
# col2.image("figures/General_Solution_Architecture_with_numbers.png", use_column_width=True, caption="Detailed Solution Architecture")  # original
# above line got this: The use_column_width parameter has been deprecated and will be removed in a future release. Please utilize the use_container_width parameter instead.
col2.image("figures/General_Solution_Architecture_with_numbers.png", use_container_width=True, caption="Detailed Solution Architecture")  # original


st.write("The numbering in the example tables below follow the numbers in the figure above.")
st.write("Note: The speech samples provided in the following tables below (Person B) are taken from a parallel database,"
         " hence they are speaking lyrics of songs. As explained in our paper, there is no requirement for the speaker "
         "to say the words of the target song or any song at all. ")
# Song 1
st.subheader('Song 1 - "Hallelujah"')
cols = st.columns(5)
cols[1].write("Segment A")
cols[2].write("Segment B")
cols[3].write("Segment C")
cols[4].write("Segment D")

row_names = ["(1) Person B - speech", "(2) Original song - mix", "(3) Original song - Instrumental solo","(4) Original song - Vocal solo","(5) SingIt style transfer"]
dir_path = "wavs/SingIt_Transfer/Song_1_Hallelujah/"
wav_df = [["person_b-m2_s5_speech_crop.wav", "person_b-m2_s5_speech_crop.wav", "person_b-m2_s5_speech_crop.wav", "person_b-m2_s5_speech_crop.wav"],
          ["1_mix_1.wav", "1_mix_2.wav", "1_mix_3.wav", "1_mix_4.wav"],
          ["2_inst_1.wav", "2_inst_2.wav", "2_inst_3.wav", "2_inst_4.wav"],
          ["3_vocal_1.wav", "3_vocal_2.wav", "3_vocal_3.wav", "3_vocal_4.wav"],
          ["4_transfer_1.wav", "4_transfer_2.wav", "4_transfer_3.wav", "4_transfer_4.wav"]]

for i in range(5):
    cols = st.columns(5)
    cols[0].write(row_names[i])
    for j in range(4):
        cols[j+1].audio(dir_path+wav_df[i][j])

st.write("Person B is 'Male 2 Song 5 - Speech' from the 'NHSS' database.")
st.write("Separation of the original audio was done by the 'Spleeter' tool.")

# Song 2
st.subheader('Song 2 - "Hey Jude"')
cols = st.columns(5)
cols[1].write("Segment A")
cols[2].write("Segment B")
cols[3].write("Segment C")
cols[4].write("Segment D")

row_names = ["(1) Person B - speech", "(2) Original song - mix", "(3) Original song - Instrumental solo","(4) Original song - Vocal solo","(5) SingIt style transfer"]
dir_path = "wavs/SingIt_Transfer/Song_2_Hey_Jude/"
wav_df = [["style-f1_s7_speech_crop.wav", "style-f1_s7_speech_crop.wav", "style-f1_s7_speech_crop.wav", "style-f1_s7_speech_crop.wav"],
          ["1_mix_1.wav", "1_mix_2.wav", "1_mix_3.wav", "1_mix_4.wav"],
          ["2_inst_1.wav", "2_inst_2.wav", "2_inst_3.wav", "2_inst_4.wav"],
          ["3_vocal_1.wav", "3_vocal_2.wav", "3_vocal_3.wav", "3_vocal_4.wav"],
          ["4_transfer_1.wav", "4_transfer_2.wav", "4_transfer_3.wav", "4_transfer_4.wav"]]

for i in range(5):
    cols = st.columns(5)
    cols[0].write(row_names[i])
    for j in range(4):
        cols[j+1].audio(dir_path+wav_df[i][j])
st.write("Person B is 'Female 1 Song 7 - Speech', and Person A is 'Male 2 Song 5 - Song' are both from the 'NHSS' database.")
st.write("The backing track was taken from [online source](https://instrumentalfx.co/the-beatles-hey-jude-instrumental/), and not done by the 'Spleeter' tool.")


# Song 3
st.subheader('Song 3 - "Billie Jean"')
cols = st.columns(5)
cols[1].write("Short segment")
cols[2].write(" ")
cols[3].write(" ")
cols[4].write(" ")

row_names = ["(1) Person B - speech", "(4) Vocal solo", "(5) SingIt style transfer"]
dir_path = "wavs/SingIt_Transfer/Song_3_Billie_Jean/"
wav_df = [["content-M1_S01_short_song_2.wav", " ", " ", " "],
          ["style-F1_Song_03_speech_2.wav", " ", " ", " "],
          ["combined-singer_M01_song_M01_S01_short_Song_2_target_F01.wav", " ", " ", " "]]

for i in range(3):
    cols = st.columns(5)
    cols[0].write(row_names[i])
    for j in range(4):
        if wav_df[i][j] == " ":
            cols[j+1].text(" ")
            continue
        cols[j+1].audio(dir_path+wav_df[i][j])
st.write("Person B is 'Female 1 Song 3 - Speech', and Person A is 'Male 1 Song 1 - Song' are both from the 'NHSS' database.")

st.markdown("""---""")
st.write("'NHSS' database: [NHSS paper](https://arxiv.org/abs/2012.00337) | [NHSS database homepage](https://hltnus.github.io/NHSSDatabase/)")
st.write("'Spleeter' tool. [Spleeter homepage](https://research.deezer.com/projects/spleeter.html) | [Spleeter GitHub](https://github.com/deezer/spleeter)")
