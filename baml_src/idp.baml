// MDOELS

class Appointment {
  day_of_week string
  month string
  date int
  year int
  hour int
  minute int
  ampm string
}


// FUNCTIONS

function ExtractAppointmentFromImage(appointment_card: image) -> Appointment {
  client "openai/gpt-4o"
  prompt #"
    {{_.role("user")}}

    Extract details from this image of an appointment card reminder:
    {{ appointment_card }}

    {{ ctx.output_format }}
  "#
}


// TESTS

test Test_APPOINTMENT {
functions [ExtractAppointmentFromImage]
  args {
    appointment_card {
      url "https://idp-baml-tutorial.s3.us-east-1.amazonaws.com/appointment.jpg"
    }
  }
}

