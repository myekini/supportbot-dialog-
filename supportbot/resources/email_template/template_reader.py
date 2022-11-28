class TemplateReader:
    def __init__(self):
        pass

    def read_course_template(self, nft_type):
        try:
            if (nft_type=='acre'):
                email_file = open("acre_balance.html", "r")
                email_message = email_file.read()
            elif (nft_type=='plot'):
                email_file = open("plot_balance.html", "r")
                email_message = email_file.read()
            elif (nft_type == 'yard'):
                email_file = open("yard_balance.html", "r")
                email_message = email_file.read()

            return email_message
        except Exception as e:
            print(f'The exception is{e}')