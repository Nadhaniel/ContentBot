import dotenv
dotenv.load_dotenv()


submission = rs.get_top_month_submissions(31)

print(submission[30])