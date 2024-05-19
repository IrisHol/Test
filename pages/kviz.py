import streamlit as st

jmeno = st.text_input("Zadej své jméno")

st.write(f"Vitejte ve vědomostním kvízu {jmeno}")

pocet_bodu = 0

st.write("1. Kolik hráčů je v olympijském curlingovém týmu?")
if st.checkbox("3"):
    st.write("0 bodů")
elif st.checkbox("4"):
    st.write("1 bod")
    pocet_bodu += 1
elif st.checkbox("5"):
    st.write("0 bodů")



st.markdown("---")

st.write("2. Jak se jmenuje největší technologická společnost v Jižní Koreji?")
if st.checkbox("Samsung"):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("LG Electronics"):
    st.write("0 bod")
elif st.checkbox("Nippon T&T"):
    st.write("0 bodů")

st.markdown("---")

st.write("3. Jaká je chemická značka vody?")
if st.checkbox("2HO"):
    st.write("0 bodů")
elif st.checkbox("HO2"):
    st.write("0 bod")
elif st.checkbox("H2O"):
    st.write("1 bodů")
    pocet_bodu += 1

st.markdown("---")

st.write("4. Kolik srdcí má chobotnice?")
if st.checkbox("Dvě"):
    st.write("0 bodů")
elif st.checkbox("Tři"):
    st.write("1 bod")
    pocet_bodu += 1
elif st.checkbox("Čtyři"):
    st.write("0 bodů")

st.markdown("---")

st.write("5. V jakém roce Beatles poprvé navštívili USA?")
if st.checkbox("1964"):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("1968"):
    st.write("0 bod")
elif st.checkbox("1966"):
    st.write("0 bodů")

st.markdown("---")

st.write("6. Který herec získal Oscara za nejlepší mužský herecký výkon za filmy Philadelphia (1993) a Forrest Gump (1994)?")
if st.checkbox("Tom Hanks"):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("Leonardi DiCaprio"):
    st.write("0 bod")
elif st.checkbox("Brad Pitt"):
    st.write("0 bodů")


st.markdown("---")

st.write("7. Který měsíc má 28 dní?")
if st.checkbox("Únor"):
    st.write("0 bodů")
elif st.checkbox("Leden"):
    st.write("0 bod")
elif st.checkbox("Všechny"):
    st.write("1 bodů")
    pocet_bodu += 1


st.markdown("---")

st.write("8. Jaké je celé jméno panenky Barbie?")
if st.checkbox("Barbara Meggie Roberts"):
    st.write("0 bodů")
elif st.checkbox("Barbara Melisa Roberts"):
    st.write("0 bod")
elif st.checkbox("Barbara Millicent Roberts"):
    st.write("1 bodů")
    pocet_bodu += 1

st.markdown("---")

st.write("9. Jak se jmenuje rostlina která vyroste až o 91 cm za den?")
if st.checkbox("Slunečnice"):
    st.write("0 bodů")
elif st.checkbox("Bambus"):
    st.write("1 bod")
    pocet_bodu += 1
elif st.checkbox("Tráva"):
    st.write("0 bodů")

st.markdown("---")

st.write("10. Co hlídá teplotu v ledničce?")
if st.checkbox("Termostat"):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("Terminál"):
    st.write("0 bod")
elif st.checkbox("Terminátor"):
    st.write("0 bodů")


st.markdown("---")
st.write(f"Gratuluji {jmeno}, váš počet bodů je: {pocet_bodu}")
if st.button ("Smazat výsledek"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()  
    #zatim nefunguje