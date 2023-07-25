import boto3

def mass_emailer(event, context):
    ses_client = boto3.client('ses', region_name='us-east-1a')  # Replace with your desired AWS region
    #Initializes SES client

    subject = event['subject']
    body = event['body']
    recipients = event['recipients']
    #Retrieve email details from event payload

    for recipient in recipients:
        try:
            message = {
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}},
                'Source': 'your-sender-email@example.com',
                # Replace with mailer-daemon later T
                'Destination': {'ToAddresses': [recipient]}
            }
            #Composes message

            response = ses_client.send_email(Message=message)
            print(f"Email sent to {recipient}: {response['MessageId']}")
            #Sends email

        except Exception as e:
            print(f"Error sending to {recipient}: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'Email sent!'
    }
    #Sends email to all recipients