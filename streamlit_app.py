import streamlit as st
from PIL import Image



image = Image.open('Raj.jpg')

st.image(image,width=400)

def main():
    st.title("My Agendas")
    st.header("Hello folks! I am Raj Mrittik and I am running for Vice President in the student council elections 2023-2024.")
    st.subheader("Please have a look at my agendas:")

    agendas = [
        "To reinstate the ATM outside the main gate, for easier student access (preferably Emirates NBD).",
        "Establish collaborations with other universities to organize inter-university workshops, promoting international exposure and knowledge exchange.",
        "Student mentors for freshmen to get them acquainted with college life and provide guidance.",
        "Renovate all college washrooms to match the standards of those near the sports complex, ensuring cleanliness and comfort.",
        "Upgrade the BITS Card recharge machine to support card tap payment and accept new currency notes for a seamless recharge process.",
        "Create a recreation room with activities like PS5, pool table, and foosball for day scholars to unwind, socialize, and relax.",
        "Enhancement of days scholars' gymnasium.",
        "Install speakers in the Activity room for clubs like Groove and Allure to enhance their practice sessions.",
        "Attempt to increase the number of devices on a student wifi connection and increase it from 2 to 3.",
        "Provide proper seating arrangement in the smoking zone and frequent cleaning for convenience and cleanliness.",
        "Open a tuck shop accessible after college hours to provide refreshments when the minimart and canteen are closed."
    ]

    st.markdown("## Agendas")
    with st.container():
        for i, agenda in enumerate(agendas):
            st.write(f"{i + 1}. {agenda}")
    
    st.markdown("---")
    st.markdown("If elected, I will be there to hear and will be your voice.")
    st.markdown("Thank you 🙏🏻")


if __name__ == "__main__":
    main()
