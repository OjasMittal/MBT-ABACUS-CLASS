import streamlit as st
from PIL import Image
from annotated_text import annotated_text
import emoji
import requests
from streamlit_lottie import st_lottie
import random

img=Image.open('icon.jpg')
st.set_page_config(page_title="MBT ABACUS CLASS",page_icon=img)
#Animation
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


with st.sidebar:
    c1,c2,c3=st.columns([1,4,1])
    with c2:
        lottie_animation_4 = "https://assets6.lottiefiles.com/packages/lf20_pbsn1omx.json"
        lottie_anime_json4 = load_lottie_url(lottie_animation_4)
        st_lottie(lottie_anime_json4,key="contact")

st.sidebar.write(":mailbox: ***Address:***   MBT Abacus Class,Shop No 13,Shri om sadguru chs, Dattatray Tandel Marg, New Sector-50, Seawoods, Navi Mumbai, Maharashtra 400706")
st.sidebar.write(":round_pushpin: <a href='https://goo.gl/maps/G19WwR18pjKeKUYM6'> **Get Directions** </a>",unsafe_allow_html=True)
st.sidebar.write(":phone: ***Contact:***  **<a href='tel:9920092640'>9920092640</a>** ~ Tulika Mittal (Center Director)",unsafe_allow_html=True)

col1,col2=st.sidebar.columns([1,4])
with col1:
    ime = Image.open('fb logo.png')
    st.image(ime,width=30)
    ima = Image.open('insta_logo.jpg')
    st.write('')
    st.image(ima,width=30)
    imb=Image.open('youtube_logo.png')
    st.write('')
    st.image(imb,width=30)
with col2:
    st.write('https://rb.gy/rju3lw')
    st.write('')
    st.write('https://rb.gy/pfdqdj')
    st.write('')
    st.write('https://surl.li/jrllj')
hide_menu_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)

st.title("***\N{brain}MBT ABACUS & HANDWRITING CLASS***\N{trophy}")


col1,col2,col3=st.columns([1,2,1])

with col2:
    lottie_animation_2 = "https://assets4.lottiefiles.com/packages/lf20_1pxqjqps.json"

    lottie_anime_json2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json2, key = "calculation")

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
col1,col2=st.columns([3,1])
with col1:
    image1 = Image.open('mastermindabacus-logo.png')
    st.image(image1, caption='Mastermind Abacus',
                 width=400)
with col2:
    lottie_animation_1 = "https://assets6.lottiefiles.com/packages/lf20_hv2s4zdr.json"

    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json, key="hello")
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
    st.video('https://youtu.be/jRfoVg34Pkk')
with col2:
    st.video('https://www.youtube.com/watch?v=Gu1zvqtXJzA')
with col3:
    st.video('https://youtu.be/2q-TMeRxmTs')
col1,col2,col3=st.columns(3)
with col1:
    st.video('https://youtu.be/XdSlHnDIg-4')
with col2:
    st.video('https://www.youtube.com/watch?v=1grEKIqDDVA&t=1s')
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
col1,col2=st.columns([2,1])
with col1:
    image2 = Image.open('write right.png')
    st.image(image2, caption='Write Right India',
                 width=400)
with col2:
    lottie_animation_3 = "https://assets9.lottiefiles.com/packages/lf20_1c4di8xm.json"
    lottie_anime_json3 = load_lottie_url(lottie_animation_3)
    st_lottie(lottie_anime_json3, key="handwriting")

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
  image3 = Image.open('sample.jpg')
  st.image(image3, caption='100% Money Back Challenge',
             width=350)
with col2:
  image4=Image.open('sample_hindi.jpg')
  st.image(image4, caption='Gift yourself a beautiful handwriting!',
             width=310)
st.subheader("Kindly fill the form below for further discussion and enrollment.")
st.info("https://forms.gle/cSgXzbG77TrdDp1B9")
st.title("GRAPHOLOGY")
st._transparent_write("Graphology is the science and art of studying handwriting patterns to understand"
                      " the subconscious mind and personality traits of an individual. It is based on the belief"
                      " that every stroke, curve, and line in one's handwriting reflects their unique character, "
                      "emotions, and attitudes. By examining various elements of handwriting, such as size, slant, "
                      "pressure, spacing, and more, we gain valuable insights into an individuals psychological makeup.")
col1,col2=st.columns(2)
with col1:
    st.image('grapho1.jpg',width=310)
with col2:
    st.image('grapho2.jpg',width=400,caption='Feedbacks')
# st.title("GUITAR")
# c1,c2=st.columns([2,1])
# with c1:
#     image5=Image.open('guitar.jpg')
#     st.image(image5, caption='Enhance your skills!',
#                  width=300)
# with c2:
#     lottie_animation_4 = "https://assets5.lottiefiles.com/packages/lf20_GmXdtd.json"
#     lottie_anime_json4 = load_lottie_url(lottie_animation_4)
#     st_lottie(lottie_anime_json4,key="guitar")
# st.write("**MBT has tied up with Plexus Academy to provide best quality guitar lessons.Classes occurs every-**")
# annotated_text(("Wednesday","from",'#8ef'),("7:00-8:30","pm","#faa"))
# st.subheader("Kindly fill the form below for further discussion and enrollment.")
# st.info("https://forms.gle/cSgXzbG77TrdDp1B9")


st.header('Review and Ratings')

imagee5 = Image.open('maps.png')
st.image(imagee5, 'Seawoods,Navi Mumbai', width=200)
url = 'https://reviewthis.biz/mbt-abacus'
st.write('***WRITE A REVIEW***')
st.write('**Click [here](%s) to give your reviews on Google Maps !!**' % url)
c1,c2,c3=st.columns(3)
with c1:
    lottie_animation_4 = "https://assets6.lottiefiles.com/datafiles/QDHTh1tUmPJvYoz/data.json"
    lottie_anime_json4 = load_lottie_url(lottie_animation_4)
    st_lottie(lottie_anime_json4, key="review")
st.subheader("Thanks for Visiting!")
st.info('This Website has been developed by an MBT Alumini. \N{slightly smiling face}')
c1,c2,c3,c4,c5,c6=st.columns(6)
num =random.randint(1, 999)
flag=False
col1,col2=st.columns([1,8])
with col1:
    if st.button(emoji.emojize(':thumbs_up:',use_aliases=True)):
        flag=True
with col2:
    if flag==False:
        st.text('⬅️ Click here for a surprise !')
if flag:
        st.success(f"**Congratulations !!** You have won a discount coupon!!\n Get **FLAT 10% off** on registration fees.\n\n **Coupon Code: MBTWEB{num}**")
        st.balloons()
        flag=False






