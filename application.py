import streamlit as st
import datetime
import json
from pathlib import Path
from streamlit_ace import st_ace

# Function to save application data
def save_application_data(application_data):
    # Convert application data to JSON format
    application_data_json = json.dumps(application_data, indent=4, sort_keys=True, default=str)
    # Define file path (you might want to include a timestamp or user identifier in the filename)
    file_path = f"applications/application_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    # Save JSON data to a file
    with open(file_path, 'w') as file:
        file.write(application_data_json)
    # Show a success message (optional, depending on your application flow)
    st.success("Application data saved successfully!")
  
# Helper function for navigation and auto-saving data
def navigate_and_save(section_data, next_page, prev_page=None, last_section=False):
    """Navigate to next or previous page and save current section's data."""
    if prev_page and st.button("Previous Section"):
        st.session_state.page_number = prev_page
    else:
        if section_data:
            st.session_state.application_data.update(section_data)
        if st.button("Next Section") or (last_section and st.button("Submit Application")):
            if last_section:
                # Save application data since this is the last section
                save_application_data(st.session_state.application_data)
            st.session_state.page_number = next_page
  
# COMPLETE FORM CONTENT
def application_form():
  """Display and manage the application form sections."""
  # Introduction
  if st.session_state.page_number == 1:
    st.title("Welcome to the PlawLabs Job Application Portal")
    st.markdown("""
                At PlawLabs, we believe in the power of technology to transform lives and redefine what's possible. We're not just a company; we're a movement of dreamers, innovators, and game-changers, determined to shape the future of tech. If you're driven by passion, curiosity, and the desire to make a monumental impact, you might just belong with us.
            """)
    if st.button("Start Application"):
      st.session_state.page_number += 1

  # Section 1: Personal Information
  elif st.session_state.page_number == 2:
      st.header("Section 1: Personal Information")
      personal_info = {
        "Full Name": st.text_input("Full Name", key="full_name"),
        "Contact Email": st.text_input("Contact Email", key="contact_email"),
        "Phone Number": st.text_input("Phone Number", key="phone_number"),
        "Current Location": st.text_input("Current Location", key="current_location"),
        "LinkedIn Profile": st.text_input("LinkedIn Profile (optional)", key="linkedin_profile"),
        "Portfolio Link": st.text_input("Portfolio Link (GitHub/Personal Website, if applicable)", key="portfolio_link"),
      }
      navigate_and_save(personal_info, next_page=3)

    # Section 2: Position and Availability
  elif st.session_state.page_number == 3:
    st.header("Section 2: Position and Availability")
    positions = [
        "AI Research Scientist", "Machine Learning Engineer", "Data Analyst",
        "Hardware Engineer", "IoT Architect", "Full Stack Developer",
        "Frontend Developer", "Backend Developer", "DevOps Engineer",
        "UI/UX Designer", "Graphic Designer", "Product Manager",
        "Marketing Strategist", "SEO Specialist", "Content Creator",
        "Business Analyst", "Financial Planner",
        "Investor Relations Manager", "Legal Counsel",
        "Human Resources Manager", "Talent Acquisition Specialist",
        "Customer Support Representative", "Sales Manager",
        "Community Manager", "Blockchain Specialist",
        "Cybersecurity Analyst", "Software Tester/QA",
        "Mobile App Developer", "Game Developer",
        "Augmented Reality Specialist", "Virtual Reality Developer",
        "Cloud Solutions Architect", "Network Engineer", "Robotics Engineer",
        "Sustainability Coordinator"
    ]

    position_info = {
        "Desired Position": st.selectbox("Desired Position", ["Select a position"] + positions, index=0, key="desired_position"),
        "Availability Date": st.date_input("Availability Date", min_value=datetime.date.today(), key="availability_date"),
        "Current Employment Status": st.radio("Current Employment Status", ["Employed", "Unemployed", "Self-Employed", "Student"], key="employment_status"),
        "Willingness to Relocate": st.radio("Willingness to Relocate", ["Yes", "No"], key="relocation"),
    }

    navigate_and_save(position_info, next_page=4, prev_page=2)

    # Section 3: Educational Background
  elif st.session_state.page_number == 4:
    st.header("Section 3: Educational Background")
    education_info = {
      "Highest Degree Earned": st.selectbox("Highest Degree Earned", ["Select a degree", "High School Diploma", "Associate Degree", "Bachelor's Degree", "Master's Degree", "Ph.D. or Higher"], index=0, key="highest_degree"),
      "Field of Study": st.text_input("Field of Study", key="field_of_study"),
      "Institution": st.text_input("Educational Institution", key="institution"),
      "Graduation Year": st.number_input("Year of Graduation", min_value=1900, max_value=datetime.date.today().year, step=1, key="graduation_year")
    }
    navigate_and_save(education_info, next_page=5, prev_page=3)

  # Section 4: Work Experience - Enhanced and Detailed
  elif st.session_state.page_number == 5:
      st.header("Section 4: Work Experience")

      # Check if 'work_experiences' is initialized in session state
      if 'work_experiences' not in st.session_state:
          st.session_state.work_experiences = []
      # Function to handle adding new work experience
      def add_work_experience():
          st.session_state.work_experiences.append({
              "Job Title": "",
              "Company Name": "",
              "Employment Duration": "",
              "Location": "",
              "Key Responsibilities": "",
              "Significant Achievements": ""
          })
      st.markdown("### Add your professional work experiences below")
      st.markdown("You can add multiple entries by clicking on 'Add another experience' button.")
      # Display experiences dynamically
      for i, experience in enumerate(st.session_state.work_experiences):
          with st.container():
              st.markdown(f"#### Experience {i + 1}")
              expander = st.expander(label="Work Experience Details", expanded=True)
              with expander:
                  experience["Job Title"] = st.text_input(f"Job Title {i+1}", experience["Job Title"])
                  experience["Company Name"] = st.text_input(f"Company Name {i+1}", experience["Company Name"])
                  experience["Employment Duration"] = st.text_input(f"Employment Duration {i+1}", experience["Employment Duration"])
                  experience["Location"] = st.text_input(f"Location {i+1}", experience["Location"])
                  experience["Key Responsibilities"] = st.text_area(f"Key Responsibilities {i+1}", experience["Key Responsibilities"])
                  experience["Significant Achievements"] = st.text_area(f"Significant Achievements {i+1}", experience["Significant Achievements"])
      # Add button to add more experiences
      if st.button("Add another experience"):
          add_work_experience()
      # Navigate and Save
      navigate_and_save(None,next_page=6,prev_page=4)
  
  # Section 5: Coding Challenge
  elif st.session_state.page_number == 6:
      st.header("Section 5: Coding Challenge")
      st.markdown("""
      ### Challenge Description
      Implement a function `is_palindrome` that checks if a given string is a palindrome. A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

      **Examples:**
      - `is_palindrome("A man, a plan, a canal: Panama")` should return `True`
      - `is_palindrome("race a car")` should return `False`

      ### Instructions
      - Select a programming language from the dropdown menu.
      - Write your solution in the code editor provided below.
      - Press the **Submit** button when you're ready to proceed.
      """)
      language_options = ["Python", "JavaScript", "Java", "C++", "Ruby"]
      language = st.selectbox("Select Language", options=language_options, index=0, key="challenge_language")
      language_modes = {
          "Python": "python",
          "JavaScript": "javascript",
          "Java": "java",
          "C++": "c_cpp",
          "Ruby": "ruby"
      }
      selected_mode = language_modes.get(language, "python")  # Default to Python if not found
      code = st_ace(language=selected_mode, theme="twilight", font_size=16, key="ace_editor_challenge", height=200) 
      if st.button("Submit Code"):
          st.session_state.application_data["Coding_Challenge_Solution"] = {"code": code, "language": language}
          st.success("Code submitted successfully.")
          navigate_and_save(section_data=None, next_page=7, prev_page=5)  

  # Section 6: Creative Submission (for Design and Content Positions)
  elif st.session_state.page_number == 7:
      st.header("Section 6: Creative Submission")
      st.markdown("""
                  ### Creative Portfolio Submission
                  We value creativity and innovation at our core. As part of your application for design or content positions, upload your design portfolio or writing samples to showcase your creativity and experience.

                  **Please ensure your files are in the correct format as described below.**
                  """)

      with st.form("creative_submission_form"):
          # Design Portfolio Upload
          design_portfolio = st.file_uploader("Upload Design Portfolio",
                                              type=['pdf', 'zip'],  # Acceptable file types
                                              help="Accepted formats: pdf, zip. Max size: 200MB")

          # Writing Samples Upload
          writing_samples = st.file_uploader("Upload Writing Samples",
                                             type=['pdf', 'doc', 'docx'],
                                             help="Accepted formats: pdf, doc, docx. Max size: 200MB")

          # Form submission
          submitted = st.form_submit_button("Submit Creative Works")

          if submitted:
              if design_portfolio is not None or writing_samples is not None:
                  # Assuming a function to handle file saving and/or processing
                  # For demo purposes, we're just acknowledging the upload.
                  st.success("Thank you for submitting your creative works.")

                  # Update session state; more intricate handling may be needed for actual files
                  st.session_state.application_data["Creative_Submission"] = {
                      "Design Portfolio": design_portfolio is not None,
                      "Writing Samples": writing_samples is not None
                  }
                  # Navigate to the next section
                  st.session_state.page_number += 1
              else:
                  st.error("Please upload at least one file to proceed.")

  # Section 7: Compensation Expectations - Enhanced
  elif st.session_state.page_number == 8:
      with st.form("Section_7"):
          st.header("Section 7: Compensation Expectations")
          st.markdown("""
                      Let us know your compensation expectations. Please specify your salary range or any other compensation requirements you deem necessary.
                  """)
          # Input for compensation expectations
          compensation_expectations = st.text_input(
              "Compensation Expectations",
              placeholder="E.g., $50,000 per year, stock options, etc.",
              key="compensation_expectations")

          submitted = st.form_submit_button("Submit")

          if submitted:
              if compensation_expectations:
                  # Save to session state
                  st.session_state.application_data["Compensation Expectations"] = compensation_expectations
                  st.success("Compensation expectations recorded.")

                  # Navigate to the next section
                  st.session_state.page_number += 1
              else:
                  st.error("Please enter your compensation expectations to proceed.")

  # Section 8: Referrals and Discovery
  elif st.session_state.page_number == 9:
      with st.form("Section_8"):
          st.header("Section 8: Referrals and Discovery")
          st.markdown("""
                      We're always curious to know how our candidates discover us. This helps us understand which channels are most effective for connecting with talents like you.
                      """)

          # Dropdown for discovery source selection
          discovery_source = st.selectbox("How did you find out about us?",
                                        options=[
                                            "Select an option",
                                            "Online Job Posting", "Referral",
                                            "Social Media", "Company Website",
                                            "Other"
                                        ],
                                        key="discovery_source")

          # Conditional input for referral name
          referral_name = ""
          if discovery_source == "Referral":
              referral_name = st.text_input(
                  "Referral Name",
                  placeholder="Please enter the name of the person who referred you.",
                  key="referral_name")

          # Form submission button
          submitted = st.form_submit_button("Submit")

          if submitted:
              if discovery_source != "Select an option":
                  # Save to session state
                  st.session_state.application_data["Referrals and Discovery"] = {
                      "Discovery Source": discovery_source,
                      "Referral Name": referral_name
                  }
                  st.success("Thank you for sharing how you found us.")

                  # Navigate to the next section
                  st.session_state.page_number += 1
              else:
                  st.error("Please select how you discovered us to proceed.")

  # Section 9: Video Introduction (Optional) - Enhanced
  elif st.session_state.page_number == 10:
      with st.form("Section_9"):
          st.header("Section 9: Video Introduction")
          st.markdown("""
                      We'd love to hear more about you in your own words! Optionally, you can upload a short video introducing yourself and explaining why you want to join PlawLabs. This is your chance to bring your application to life and showcase your personality beyond the traditional resume.

                      **Please keep your video to under 2 minutes.**

                      **Acceptable Formats:** mp4, mov, avi
                      """)

          # Enhanced file uploader for video introduction with format and size constraints
          video_introduction_upload = st.file_uploader("Upload Video Introduction",
                                                       type=['mp4', 'mov', 'avi'],
                                                       accept_multiple_files=False,
                                                       help="Max size: 200MB")

          # Validation and feedback for file upload
          if video_introduction_upload is not None:
              file_size_MB = video_introduction_upload.size / (1024 * 1024) # Convert bytes to MB
              if file_size_MB > 200:
                  st.error("The uploaded file exceeds the 200MB size limit. Please upload a smaller file.")
              else:
                  submitted = st.form_submit_button("Submit")
                  if submitted:
                      # For demo, we acknowledge the upload. In a real scenario, you'd handle the file appropriately.
                      st.success("Thank you for submitting your video introduction.")

                      # Save video file info to session state; actual files need special handling
                      st.session_state.application_data["Video_Introduction"] = {
                          "Uploaded": True,
                          "File Name": video_introduction_upload.name
                      }
                      st.session_state.page_number += 1
          else:
              st.info("Video upload is optional but highly recommended.")
              if st.form_submit_button("Skip and continue"):
                  # Navigate forward with indication that video was skipped
                  st.session_state.application_data["Video_Introduction_Skipped"] = True
                  st.session_state.page_number += 1
  
  # Section 10: Questions for PlawLabs - Enhanced
  elif st.session_state.page_number == 11:
      with st.form("Section_10"):
          st.header("Section 10: Questions for PlawLabs")
          st.markdown("""
                      Your aspirations and questions are important to us. This section is your opportunity to tell us more about where you see yourself in the future and to ask any questions you might have about working at PlawLabs.

                      Your insightful responses will help us understand your long-term career goals and how PlawLabs might support them.
                      """)

          long_term_career_aspirations = st.text_area(
              "What are your long-term career aspirations?",
              placeholder="Share your career goals and how you think PlawLabs fits into them.",
              help="Think about where you'd like to see yourself professionally in 5, 10, or 15 years."
          )

          handling_pressure = st.text_area(
              "How do you handle working under pressure with tight deadlines?",
              placeholder="Provide an example or describe your approach.",
              help="Describe situations where you've thrived under pressure or managed tight deadlines effectively."
          )

          # Additional question for thorough insight
          what_attracts_you_to_plawlabs = st.text_area(
              "What attracts you to PlawLabs?",
              placeholder="Describe what excites you about the possibility of working with PlawLabs.",
              help="This can include the company culture, mission, projects, or technology stack."
          )

          submitted = st.form_submit_button("Submit")
          if submitted:
              if long_term_career_aspirations and handling_pressure and what_attracts_you_to_plawlabs:
                  # Save responses in session state
                  st.session_state.application_data["Questions for PlawLabs"] = {
                      "Long-Term Career Aspirations": long_term_career_aspirations,
                      "Handling Pressure": handling_pressure,
                      "What Attracts You to PlawLabs": what_attracts_you_to_plawlabs
                  }
                  st.success("Responses submitted successfully.")
                  st.session_state.page_number += 1
              else:
                  st.error("Please provide an answer to all the questions to proceed.")

  # Section 11: Legal Confirmations - Enhanced
  elif st.session_state.page_number == 12:
      with st.form("Section_11"):
          st.header("Section 11: Legal Confirmations")
          st.markdown("""
                      Before you continue, we need to confirm a few legal necessities. Your honesty in these confirmations is crucial for the application process.
                      """)

          # Capture confirmation of work authorization
          work_authorization = st.radio(
              "Do you have the authorization to work in the country where the job is located?",
              ["Yes", "No"],
              help="This information is required to verify your eligibility for employment in the job's location."
          )

          # Capture agreement to terms and conditions
          agreement = st.checkbox(
              "I agree to the Terms and Conditions.",
              help="Please read the Terms and Conditions carefully before agreeing."
          )

          # Ensure that agreement checkbox is marked
          submitted = st.form_submit_button("Submit")
          if submitted:
              if agreement:  # Check that the agreement box is checked
                  # Save legal confirmations in session state
                  st.session_state.application_data["Legal Confirmations"] = {
                      "Work Authorization": work_authorization,
                      "Agreement to Terms": agreement
                  }
                  st.success("Legal confirmations submitted successfully.")
                  st.session_state.page_number += 1
              else:
                  st.error("You must agree to the Terms and Conditions to proceed.")

  # Section 12: Diversity and Inclusion - Enhanced Version
  elif st.session_state.page_number == 13:
      with st.form("Section_12"):    
          st.header("Section 12: Diversity and Inclusion")
          st.markdown("""
          #### We Value Diversity
          At PlawLabs, we're committed to creating an inclusive environment. This information helps us understand the diversity of our candidates. Participation is voluntary and has no effect on your application. 
          \n*Your responses will be treated with confidentiality.*
          """)

          diversity_options = [
              "Female",
              "Male",
              "I prefer to self-describe", 
              "Other"
          ]
          diversity = st.selectbox("Your Gender Identity:", options=diversity_options, index=0, key="diversity")

          if diversity == "I prefer to self-describe" or diversity == "Other":
              self_describe_input = st.text_input("Please describe (optional):", key="self_describe")

          submitted = st.form_submit_button("Submit")
          if submitted:
              diversity_info = {"Diversity": diversity}
              if diversity in ["I prefer to self-describe", "Other"]:
                  diversity_info["Self-Description"] = self_describe_input if 'self_describe' in st.session_state else ''

              st.session_state.application_data["Diversity and Inclusion"] = diversity_info
              st.session_state.page_number += 1
              st.success("Diversity and Inclusion information submitted.")

  # Section 13: Additional Information - Enhanced
  elif st.session_state.page_number == 14:
      with st.form("Section_13"):
          st.header("Section 13: Additional Information")
          st.markdown("""
                      Here, we invite you to share anything else you'd like us to know about you. This might include unique skills or experiences, personal projects, extracurricular activities, motivations for applying, or clarifications regarding previous sections of this application.
                      \nFeel free to include anything you believe strengthens your application or helps us understand you better.
                      """)

          additional_info = st.text_area(
              "Any additional information you'd like to share with us?",
              placeholder="Type here...",
              help="This section is optional but can be valuable in providing a more complete picture of your candidacy.",
              key="additional_info"
          )

          submitted = st.form_submit_button("Submit Additional Information")
          if submitted:
              if additional_info:  # Check if the user has provided any additional information
                  st.session_state.application_data["Additional Information"] = {"Additional Information": additional_info}
                  st.success("Your additional information has been submitted successfully.")
                  st.session_state.page_number += 1
              else:
                  # It's okay to not have any additional info, but we still navigate them forward after a click
                  st.session_state.application_data["Additional Information"] = {"Additional Information": "N/A"}
                  st.info("No additional information provided. Proceeding to the next section.")
                  st.session_state.page_number += 1

# Section 14: Confirmation and Submission
  elif st.session_state.page_number == 15:
      with st.form("Section_14"):
          st.header("Section 14: Confirmation")
  
          # Preview the collected application data for user to review
          st.json(st.session_state.application_data)
  
          # Confirmation checkbox
          confirmation = st.checkbox(
              "I hereby confirm that all information entered is correct to the best of my knowledge and belief."
          )
  
          # Submit button for the form
          submitted = st.form_submit_button("Submit Application")
          if submitted:
              if confirmation:
                  # Save application data using the designated function
                  save_application_data(st.session_state.application_data)
  
                  st.success("Your application has been successfully submitted! Thank you for applying.")
  
                  # Optionally clear session state to reset the application form
                  for key in list(st.session_state.keys()):
                      del st.session_state[key]  # Clear each key to reset the form
  
              else:
                  st.error("You must confirm the accuracy of your information before submitting.")
