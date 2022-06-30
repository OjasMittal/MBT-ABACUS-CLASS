import streamlit as st
from PIL import Image
from annotated_text import annotated_text
import emoji


img=Image.open('icon.jpg')
st.set_page_config(page_title="MBT ABACUS CLASS",page_icon=img)

c1,c2,c3,c4,c5,c6=st.sidebar.columns(6)
with c2:
  st.image(img, caption='MBT ABACUS CLASS',width=190)
st.sidebar.title(" CONTACT INFORMATION :")
st.sidebar.write(":mailbox: ***Address:***   MBT Abacus Class,Shop No 13,Shri om sadguru chs, Dattatray Tandel Marg, New Sector-50, Seawoods, Navi Mumbai, Maharashtra 400706")
st.sidebar.write(":phone: ***Contact:***  **9920092640** ~ Tulika Mittal (Center Director)")
col1,col2=st.sidebar.columns([1,4])
with col1:
    ime = Image.open('fb logo.png')
    st.image(ime,
             width=30)
    ima = Image.open('insta_logo.jpg')
    st.image(ima,
             width=30)
with col2:
    st.write('https://rb.gy/rju3lw')
    st.write('https://rb.gy/pfdqdj')
hide_menu_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)

st.title("***\N{brain}MBT ABACUS CLASS***\N{trophy}")
st.write("***MBT Abacus Class was started in the year 2014 by Mrs.Tulika Mittal with a "
             "hope to provide something good to the society and promote women entrepreneurship.***")
col1,col2=st.columns(2)
with col1:
    ige = Image.open('mom_web.jpg')
    st.image(ige, caption='Tulika Mittal',
             width=300)
with col2:
    ige = Image.open('class.png')
    st.image(ige, caption='Seawoods Center',
             width=400)
st.write("MBT is authorised franchise of **Mastermind** and **WriteRight-India** and is known to provide quality education with various kinds of courses like **Abacus,"
             "Handwriting improvement,Speed Writing,Calligraphy and Guitar.**")
image = Image.open('class.jpg')
st.image(image, caption='MBT ABACUS CLASS,SEAWOODS,NAVI MUMBAI',
             width=400)
st.title("ABACUS")
image1 = Image.open('mastermindabacus-logo.png')
st.image(image1, caption='Mastermind Abacus',
             width=400)
st.write("**Finding a quality Abacus academy for a child is not easy, as parents are not"
             " aware of the intricacies of Abacus training & learning.MBT is the Navi Mumbai Master Franchise of Mastermind Abacus.**")
col1,col2=st.columns(2)
with col1:
    imge2 = Image.open('benifits.jpg')
    st.image(imge2,width=300)
with col2:
    imge2 = Image.open('abacus1.jpg')
    st.image(imge2, width=400)
st.write("**When a child learns Abacus, parents expect improvement in their mental "
             "math abilities. In addition, they expect enhanced listening ability, visualization capacity, and "
             "concentration levels in their children.**")
col1,col2=st.columns(2)
with col1:
  imge1 = Image.open('ab.jpg')
  st.image(imge1,width=300)
with col2:
  imge1 = Image.open('images.jpg')
  st.image(imge1, width=350)

col1,col2=st.columns(2)
with col1:
    imge1 = Image.open('images (1).jpg')
    st.image(imge1, width=300)

with col2:
    imge1 = Image.open('img3.jpg')
    st.image(imge1, width=350)


st.write("**They expect whole-brain development and increased confidence "
             "in the child. Also, overall performance in Academics should reflect their improved abilities**")


col1,col2,col3=st.columns(3)
with col1:
    st.video('https://youtu.be/6eFyspBqvNE')
with col2:
    st.video('https://www.youtube.com/watch?v=Gu1zvqtXJzA')
with col3:
    st.video('https://www.youtube.com/watch?v=9GoGHxOjGtA')
col1,col2,col3=st.columns(3)
with col1:
    st.video('https://www.youtube.com/watch?v=a9BnNWrzHY4')
with col2:
    st.video('https://www.youtube.com/watch?v=1grEKIqDDVA')
with col3:
    st.video('https://www.youtube.com/watch?v=VbG92I6cp1Q')
st.write(
        " ***Furthermore, Mastermind's game-based program ensures the learning process does not become monotonous, "
        "which is very important for the expected results.***")
annotated_text(("Age  Criteria ", ":","#8ef"),("5-14 years"," ","#faa"))
st.write(" ")
annotated_text(("Duration", ":","#8ef"),("8 levels of 3 months each and 2 advanced levels  with once-in-a-week classes of two hours."," ","#faa"))
st.write(" ")
annotated_text(("Method", ":","#8ef"),("Fun & Learn Method with special speed building software mobile app"," ","#faa"))
st.write(" ")
st.subheader("Kindly fill the form below for further discussion and enrollment.")
st.info("https://forms.gle/cSgXzbG77TrdDp1B9")
st.title("HANDWRITING")
image2 = Image.open('write right.png')
st.image(image2, caption='Write Right India',
             width=400)
st.header("***Handwriting Can Be Improved At Any Age!***")
st.write("**But, the fact is that Handwriting invariably, can be corrected at any age."
             " The only condition applied is that the writer should have steady hands.**")
st.write("***MBT is an authorized franchise of Write Right India and offers 3 types of handwriting courses:***")
annotated_text(("1.Handwriting Improvement",":","#8ef"),("Improve your handwriting within 7 days with 100% money back guarantee"," ","#faa"))
st.write(" ")
annotated_text(("2.Calligraphy",":","#8ef"),("Learn various fonts of Calligraphy and score full marks in your projects just in 15 days!!"," ","#faa"))
st.write(" ")
annotated_text(("3.Speed Writing",":","#8ef"),("Loosing marks in exams due to lack of time?  Dont worry, just improve your writing speed with our certified "
             "course of speed writing and complete your exam faster than others!!"," ","#faa"))
st.write(" ")
st.header(" ")
col1,col2=st.columns(2)
with col1:
  image3 = Image.open('handwr.jpg')
  st.image(image3, caption='100% Money Back Challenge',
             width=350)
with col2:
  image4=Image.open('handwriting.jpg')
  st.image(image4, caption='Gift yourself a beautiful handwriting!',
             width=350)
st.subheader("Kindly fill the form below for further discussion and enrollment.")
st.info("https://forms.gle/cSgXzbG77TrdDp1B9")
st.title("GUITAR")
image5=Image.open('guitar.jpg')
st.image(image5, caption='Enhance your skills!',
             width=300)
st.write("**MBT has tied up with Plexus Academy to provide best quality guitar lessons.Classes occurs every-**")
annotated_text(("Wednesday","from",'#8ef'),("7:00-8:30","pm","#faa"))
st.subheader("Kindly fill the form below for further discussion and enrollment.")
st.info("https://forms.gle/cSgXzbG77TrdDp1B9")


st.header('Review and Ratings')
imagee5 = Image.open('maps.png')
st.image(imagee5, 'Seawoods,Navi Mumbai', width=200)
url = 'https://reviewthis.biz/mbt-abacus'
st.write('***WRITE A REVIEW***')
st.write('**Click [here](%s) to give your reviews on Google Maps**' % url)
st.subheader("Thanks for Visiting!")
st.info('This Website has been developed by an MBT Alumini. \N{slightly smiling face}')
c1,c2,c3,c4,c5,c6=st.columns(6)
with c1:
   if st.button(emoji.emojize(':thumbs_up:',use_aliases=True)):
        st.balloons()






