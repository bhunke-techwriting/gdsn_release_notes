import re
import streamlit as st


# Define the regular expressions to search for and their replacements
patterns = [
    (r'<p>', '<p style="margin: 5px 0;line-height: 1.5;">'),
    (r'<p .*?>', '<p style="margin: 5px 0;line-height: 1.5;">'),
    (r'<li.*?>', '<li style="margin: 5px 0;line-height: 1.5;">'),
    (r'</?span.*?>', ''),
    (r'<h1.*?>', '<h1 style="margin: 20px 0;line-height: 1.5;font-size: 30px;font-weight: 400;">'),
    (r'<h2.*?>', '<h2 style="margin: 20px 0;line-height: 1.5;font-size: 24px;font-weight: 400;">'),
    (r'<h3.*?>', '<h3 style="margin: 20px 0;line-height: 1.5;font-size: 20px;font-weight: 400;">'),
    (r'<h4.*?>', '<h4 style="margin: 20px 0;line-height: 1.5;font-size: 18px;font-weight: 700;">'),
    (r'<table.*?>', '<table border="1" class="table-bordered" style="word-wrap: break-word; width:100%; margin: 20px 0;border-collapse:collapse;">'),
    (r'<img ', '<img class="img-responsive fr-fic fr-dii" style="max-width:100%;" '),
    (r'<p style="margin: 20px 0;line-height: 1.5;"><p style="margin: 20px 0;line-height: 1.5;">', '<p style="margin: 20px 0;line-height: 1.5;">'),
]

# Define the function to apply the substitutions
def apply_substitutions(input_text):

    # Apply the <strong> substitution for <span> tags
    text = re.sub(r'<span style="font-weight:700">(.*?)</span>', r'<strong>\1</strong>', input_text)

    # Apply the <i> substitution for <span> tags
    text = re.sub(r'<span style="font-style:italic">(.*?)</span>', r'<i>\1</i>', text)


# Set up the Streamlit app
def main():
    st.title('Transform GDSN Release Notes HTML')

    # Create the input box for the user to paste in HTML
    input_text = st.text_area('Input GDSN Release Notes HTML here', height=200)

    # Create the button to apply the substitutions
    if st.button('Transform'):
        output_text = apply_substitutions(input_text)
        # Display the transformed HTML
        st.text_area('Transformed HTML', value=output_text, height=200)

if __name__ == "__main__":
    main()    
