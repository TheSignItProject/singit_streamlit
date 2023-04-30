import streamlit as st
st.set_page_config(page_title="SingIt! Singer Voice Transformation", layout="centered")
st.title("SingIt! Singer Voice Transformation")

col1, col2 = st.columns([5, 4])
col1.markdown("**Abstract:** In this paper, we propose a model which can generate a singing voice from normal speech utterance by harnessing zero-shot, many-to-many style transfer learning. Our goal is to give anyone the opportunity to sing any song in a timely manner. We present a system comprising several available blocks, as well as a modified auto-encoder, and show how this highly-complex challenge can be achieved by tailoring rather simple solutions together. We demonstrate the applicability of the proposed system using a group of 25 non-expert listeners. Samples of the data generated from our model are provided.")
col2.write(" \n")
col2.write(" \n")
col2.write(" \n")
col2.write(" \n")
col2.image("figures/High_level_overview.png", caption="High level system overview")

st.markdown("""---""")

# Section 1 - SingIt Transfer
st.header('SingIt Style Transfer Examples')

col1, col2, col3 = st.columns([1, 5, 1])
col2.image("figures/General_Solution_Architecture_with_numbers.png", use_column_width=True, caption="Detailed Solution Architecture")

st.write("The numbering in the example tables below follow the numbers in the figure above.")
# Song 1
st.subheader('Song 1 - "Hallelujah"')
cols = st.columns(5)
cols[1].write("Segment A")
cols[2].write("Segment B")
cols[3].write("Segment C")
cols[4].write("Segment D")

row_names = ["(1) Person B - speech", "(2) Original song", "(3) Instrumental solo","(4) Vocal solo","(5) SingIt transfer"]
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
st.write("Person B is 'Male 2 Song 5 Speech' from the 'NHSS' database. Separation of the original audio was done by the 'Spleeter' tool")

# Song 2
st.subheader('Song 2 - "Hey Jude"')
cols = st.columns(5)
cols[1].write("Segment A")
cols[2].write("Segment B")
cols[3].write("Segment C")
cols[4].write("Segment D")

row_names = ["(1) Person B - speech", "(2) Original song", "(3) Instrumental solo","(4) Vocal solo","(5) SingIt transfer"]
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
st.write("Person B is 'Female 1 Song 7 Speech', and Person A is 'Male 2 Song 5 Song' are both from the 'NHSS' database.")
st.write("The backing track was taken from online source, and not done by the 'Spleeter' tool.")

# Song 3
st.subheader('Song 3 - "Billie Jean"')
cols = st.columns(5)
cols[1].write("Short segment")
cols[2].write(" ")
cols[3].write(" ")
cols[4].write(" ")

row_names = ["(1) Person B - speech", "(4) Vocal solo", "(5) SingIt transfer"]
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
st.write("Person B is 'Female 1 Song 3 Speech', and Person A is 'Male 1 Song 1 Song' are both from the 'NHSS' database.")

st.markdown("""---""")

# Section 2 - Further Audio Samples
st.header('Further Audio Samples')

st.subheader('Spleeter')
st.write("The following audio samples present the capabilities of the 'Spleeter' tool incorporated in the system.")
st.markdown("‘Spleeter’ - a Python package that receives a song (mix of vocals and instruments) as an input and can separate the song into different stems (channels).")
st.markdown("[Spleeter homepage](https://research.deezer.com/projects/spleeter.html) | [Spleeter GitHub](https://github.com/deezer/spleeter)")
cols = st.columns(5)
cols[1].write("Original")
cols[2].write("Instrumental")
cols[3].write("Vocal")
cols[3].write(" ")

row_names = ["Beautiful - Christina Aguilera", "My Way - Frank Sinatra", "Nessum Dorma - Luciano Pavarotti", "Yesterday - The Beatles"]
dir_path = "wavs/Spleeter/"
wav_df = [["spleeter_christina_aguilera_beautiful.mp3", "spleeter_christina_aguilera_beautiful-instrumental.mp3", "spleeter_christina_aguilera_beautiful-vocals.mp3", " "],
          ["spleeter_frank_sinatra_my_way.mp3", "spleeter_frank_sinatra_my_way-instrumental.mp3", "spleeter_frank_sinatra_my_way-vocals.mp3", " "],
          ["spleeter_Luciano_Pavarotti_nessun_dorma.mp3", "spleeter_Luciano_Pavarotti_nessun_dorma-instrumental.mp3", "spleeter_Luciano_Pavarotti_nessun_dorma-vocals.mp3", " "],
          ["spleeter_The_Beatles_yesterday.mp3", "spleeter_The_Beatles_yesterday-instrumental.mp3", "spleeter_The_Beatles_yesterday-vocals.mp3", " "]]

for i in range(4):
    cols = st.columns(5)
    cols[0].write(row_names[i])
    for j in range(4):
        if wav_df[i][j] == " ":
            cols[j+1].text(" ")
            continue
        cols[j+1].audio(dir_path+wav_df[i][j])
st.markdown("""---""")


# NHSS
st.subheader('NHSS Dataset')
st.markdown("NHSS - a database of parallel recordings of speech and singing. The audio recordings in the NHSS database correspond to a total of 100 songs sung and spoken by 10 singers, 5 male, and 5 female, resulting in a total of 7 hours of audio data.")
st.markdown("[NHSS paper](https://arxiv.org/abs/2012.00337) | [NHSS database homepage](https://hltnus.github.io/NHSSDatabase/)")

cols = st.columns(5)
cols[1].write("Speech")
cols[2].write("Singing")
cols[3].write(" ")
cols[4].write(" ")

row_names = ["Female 2", "Female 3", "Female 4", "Male 1", "Male 3", "Male 5"]
dir_path = "wavs/NHSS/"
wav_df = [["NHSS_f2_s6_speech.mp3", "NHSS_f2_s6_song.mp3", " ", " "],
          ["NHSS_f3_s4_speech.mp3", "NHSS_f3_s4_song.mp3", " ", " "],
          ["NHSS_f4_s3_speech.mp3", "NHSS_f4_s3_song.mp3", " ", " "],
          ["NHSS_m1_s3_speech.mp3", "NHSS_m1_s3_song.mp3", " ", " "],
          ["NHSS_m3_s5_speech.mp3", "NHSS_m3_s5_song.mp3", " ", " "],
          ["NHSS_m5_s5_speech.mp3", "NHSS_m5_s5_song.mp3", " ", " "]]
for i in range(6):
    cols = st.columns(5)
    cols[0].write(row_names[i])
    for j in range(4):
        if wav_df[i][j] == " ":
            cols[j+1].text(" ")
            continue
        cols[j+1].audio(dir_path+wav_df[i][j])
