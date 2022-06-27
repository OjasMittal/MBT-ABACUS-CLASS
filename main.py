import streamlit as st
from PIL import Image

img=Image.open('icon.jpg')
st.set_page_config(page_title="MBT ABACUS CLASS",page_icon=img)
st.sidebar.image(img, caption='MBT ABACUS CLASS',width=250)
st.sidebar.title("CONTACT INFORMATION :")
st.sidebar.subheader("Address:   MBT Abacus Class,Shop No 13,Shri om sadguru chs, Dattatray Tandel Marg, New Sector-50, Seawoods, Navi Mumbai, Maharashtra 400706")
st.sidebar.subheader("Contact:  9920092640 ~ Tulika Mittal (Center Director)")
ime = Image.open('fb logo.png')
st.sidebar.image(ime,
             width=40)
st.sidebar.subheader("Facebook Page: https://rb.gy/rju3lw")

hide_menu_style="""
<style>
MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)

st.title("MBT ABACUS CLASS \N{trophy}")
st.subheader(" ")
st.subheader("MBT Abacus Class was started in the year 2014 by Mrs.Tulika Mittal with a "
             "hope to provide something good to the society and promote women entrepreneurship.")
ige = Image.open('mom.jpg')
st.image(ige, caption='Tulika Mittal',
             width=300)
st.subheader("MBT is authorised franchise of Mastermind and WriteRight India and is known to provide quality education with various kinds of courses like Abacus,"
             "Handwriting improvement,Speed Writing,Calligraphy and Guitar.")
image = Image.open('class.jpg')
st.image(image, caption='MBT ABACUS CLASS,SEAWOODS,NAVI MUMBAI',
             width=500)
st.title("Abacus")
image1 = Image.open('mastermindabacus-logo.png')
st.image(image1, caption='Mastermind Abacus',
             width=400)
st.subheader("Finding a quality Abacus academy for a child is not easy, as parents are not"
             " aware of the intricacies of Abacus training & learning.MBT is the Navi Mumbai Master Franchise of Mastermind Abacus.")
imge2 = Image.open('benifits.jpg')
st.image(imge2,width=300)
st.subheader("When a child learns Abacus, parents expect improvement in their mental "
             "math abilities. In addition, they expect enhanced listening ability, visualization capacity, and "
             "concentration levels in their children.")
st.subheader("They expect whole-brain development and increased confidence "
             "in the child. Also, overall performance in Academics should reflect their improved abilities")
imge1 = Image.open('ab.jpg')
st.image(imge1,width=400)
st.subheader(" Furthermore, Mastermind's game-based program ensures the learning process does not become monotonous, "
             "which is very important for the expected results.")

st.video('https://youtu.be/6eFyspBqvNE')
st.subheader("Age  Criteria : 5 to 14 years")
st.subheader("Duration : 8 levels of 3 months each and 2 advanced levels  with once-in-a-week classes of two hours.")
st.subheader("Method : Fun & Learn Method with special speed building software mobile app")

st.subheader("Kindly fill the form below for further discussion and enrollment.")
st.info("https://forms.gle/cSgXzbG77TrdDp1B9")
st.title("Handwriting Improvement")
image2 = Image.open('write right.png')
st.image(image2, caption='Write Right India',
             width=400)
st.subheader("Handwriting Can Be Improved At Any Age!")
st.subheader("But, the fact is that Handwriting invariably, can be corrected at any age."
             " The only condition applied is that the writer should have steady hands.")
st.subheader("MBT is an authorized franchise of Write Right India and offers 3 types of handwriting courses:")
st.subheader("1.Handwriting Improvement-Improve your handwriting within 7 days with 100% money back guarantee")
st.subheader("2.Calligraphy-Learn various fonts of Calligraphy and score full marks in your projects just in 15 days!!")
st.subheader("3.Speed Writing- Loosing marks in exams due to lack of time?"
             " Dont worry, just improve your writing speed with our certified "
             "course of speed writing and complete your exam faster than others!! :smile:")
image3 = Image.open('handwr.jpg')
st.image(image3, caption='100% Money Back Challenge',
             width=400)
image4=Image.open('handwriting.jpg')
st.image(image4, caption='Gift yourself a beautiful handwriting!',
             width=400)
st.subheader("Kindly fill the form below for further discussion and enrollment.")
st.info("https://forms.gle/cSgXzbG77TrdDp1B9")
st.title("Guitar")
image5=Image.open('guitar.jpg')
st.image(image5, caption='Enhance your skills!',
             width=300)
st.subheader("MBT has tied up with Plexus Academy to give best quality guitar lessons to students.Classes occurs every Wednesday from 7-8:30 pm")
st.subheader("Kindly fill the form below for further discussion and enrollment.")
st.info("https://forms.gle/cSgXzbG77TrdDp1B9")
st.subheader(" Thanks for Visiting!")
st.info('This Website has been developed by a MBT Alumini. \N{slightly smiling face}')




