import streamlit as st

jmeno = st.text_input("Zadej své jméno")

st.write(f"Vitejte ve vědomostním kvízu {jmeno}")

pocet_bodu = 0

st.write("1. Kolik hráčů je v olympijském curlingovém týmu?")
if st.checkbox("3", key="1a", value=False):
    st.write("0 bodů")
elif st.checkbox("4", key="1b", value=False):
    st.write("1 bod")
    pocet_bodu += 1
elif st.checkbox("5", key="1c", value=False):
    st.write("0 bodů")



st.markdown("---")

st.write("2. Jak se jmenuje největší technologická společnost v Jižní Koreji?")
if st.checkbox("Samsung", key="2a", value=False):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("LG Electronics", key="2b", value=False):
    st.write("0 bod")
elif st.checkbox("Nippon T&T", key="2c", value=False):
    st.write("0 bodů")

st.markdown("---")

st.write("3. Jaká je chemická značka vody?")
if st.checkbox("2HO", key="3a", value=False):
    st.write("0 bodů")
elif st.checkbox("HO2", key="3b", value=False):
    st.write("0 bod")
elif st.checkbox("H2O", key="3c", value=False):
    st.write("1 bodů")
    pocet_bodu += 1

st.markdown("---")

st.write("4. Kolik srdcí má chobotnice?")
if st.checkbox("Dvě", key="4a", value=False):
    st.write("0 bodů")
elif st.checkbox("Tři", key="4b", value=False):
    st.write("1 bod")
    pocet_bodu += 1
elif st.checkbox("Čtyři", key="4c", value=False):
    st.write("0 bodů")

st.markdown("---")

st.write("5. V jakém roce Beatles poprvé navštívili USA?")
if st.checkbox("1964", key="5a", value=False):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("1968", key="5b", value=False):
    st.write("0 bod")
elif st.checkbox("1966", key="5c", value=False):
    st.write("0 bodů")

st.markdown("---")

st.write("6. Který herec získal Oscara za nejlepší mužský herecký výkon za filmy Philadelphia (1993) a Forrest Gump (1994)?")
if st.checkbox("Tom Hanks", key="6a", value=False):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("Leonardi DiCaprio", key="6b", value=False):
    st.write("0 bod")
elif st.checkbox("Brad Pitt", key="6c", value=False):
    st.write("0 bodů")


st.markdown("---")

st.write("7. Který měsíc má 28 dní?")
if st.checkbox("Únor", key="7a", value=False):
    st.write("0 bodů")
elif st.checkbox("Leden", key="7b", value=False):
    st.write("0 bod")
elif st.checkbox("Všechny", key="7c", value=False):
    st.write("1 bodů")
    pocet_bodu += 1


st.markdown("---")

st.write("8. Jaké je celé jméno panenky Barbie?")
if st.checkbox("Barbara Meggie Roberts", key="8a", value=False):
    st.write("0 bodů")
elif st.checkbox("Barbara Melisa Roberts", key="8b", value=False):
    st.write("0 bod")
elif st.checkbox("Barbara Millicent Roberts", key="8c", value=False):
    st.write("1 bodů")
    pocet_bodu += 1

st.markdown("---")

st.write("9. Jak se jmenuje rostlina která vyroste až o 91 cm za den?")
if st.checkbox("Slunečnice", key="9a", value=False):
    st.write("0 bodů")
elif st.checkbox("Bambus", key="9b", value=False):
    st.write("1 bod")
    pocet_bodu += 1
elif st.checkbox("Tráva", key="9c", value=False):
    st.write("0 bodů")

st.markdown("---")

st.write("10. Co hlídá teplotu v ledničce?")
if st.checkbox("Termostat",key="10a", value=False):
    st.write("1 bodů")
    pocet_bodu += 1
elif st.checkbox("Terminál", key="10b", value=False):
    st.write("0 bod")
elif st.checkbox("Terminátor", key="10c", value=False):
    st.write("0 bodů")


st.markdown("---")

if st.button("Zobrazit výsledek", key="Zobrazit výsledek"):
    st.write(f"Gratuluji {jmeno}, váš počet bodů je: {pocet_bodu}")
