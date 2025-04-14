from stack_overflow import StackOverflow
from user import User
from search import SearchStrategy
from tag import Tag

stack_overflow = StackOverflow()
user1 = User("Siri", "Duggineni")
user2 = User("Pranavi", "Sriya")
user3 = User("Iqbal", "Shaik")

stack_overflow.add_user(user3)
stack_overflow.add_user(user2)
stack_overflow.add_user(user1)

q1 = stack_overflow.post_question(user1, "Hello")
q1.add_tag(Tag.SIRI)
q2 = stack_overflow.post_question(user1, "MACHINE learning question")
q2.add_tag(Tag.ML)
q2.add_tag(Tag.PYTHON)
ans1 = stack_overflow.post_answer(q1, user2, "Hii")
q1.up_vote()
stack_overflow.comment_on(q1, user3, "it's not social media bruh")
ans1.up_vote()
ans1.down_vote()

print(stack_overflow.search_on(Tag.PYTHON, SearchStrategy.TAG))

print(stack_overflow.search_on("Hello", SearchStrategy.KEYWORD))

print(stack_overflow.search_on(user2, SearchStrategy.USERID))
