



# This is the end of the file we wrote together

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

