def main():
  print()
  print("This program is an implementation of the Rosenberg")
  print("Self-Esteem Scale. This program will show you ten")
  print("statements that you could possibly apply to yourself.")
  print("Please rate how much you agree with each of the")
  print("statements by responding with one of these four letters:")
  print()
  print("D means you strongly disagree with the statement.")
  print("d means you disagree with the statement.")
  print("a means you agree with the statement.")
  print("A means you strongly agree with the statement.")
  print()

  score = 0

  def get_one():
    nonlocal score
    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    one = input("Enter D, d, a, or A: ")
    if one == "D":
        score += 0
    elif one == "d":
        score += 1
    elif one == "a":
        score += 2
    elif one == "A":
        score += 3
    else:
        print("Please enter a valid response.")
        get_one()
    return score

  def get_two():
      nonlocal score
      print("2. I feel that I have a number of good qualities.")
      two = input("Enter D, d, a, or A: ")
      if two == "D":
          score += 0
      elif two == "d":
          score += 1
      elif two == "a":
          score += 2
      elif two == "A":
          score += 3
      else:
          print("Please enter a valid response.")
          get_two()
      return score

  def get_three():
      nonlocal score
      print("3. All in all, I am inclined to feel that I am a failure.")
      three = input("Enter D, d, a, or A: ")
      if three == "D":
          score += 3
      elif three == "d":
          score += 2
      elif three == "a":
          score += 1
      elif three == "A":
          score += 0
      else:
          print("Please enter a valid response.")
          get_three()
      return score

  def get_four():
      nonlocal score
      print("4. I am able to do things as well as most other people.")
      four = input("Enter D, d, a, or A: ")
      if four == "D":
          score += 0
      elif four == "d":
          score += 1
      elif four == "a":
          score += 2
      elif four == "A":
          score += 3
      else:
          print("Please enter a valid response.")
          get_four()
      return score

  def get_five():
      nonlocal score
      print("5. I feel I do not have much to be proud of.")
      five = input("Enter D, d, a, or A: ")
      if five == "D":
          score += 3
      elif five == "d":
          score += 2
      elif five == "a":
          score += 1
      elif five == "A":
          score += 0
      else:
          print("Please enter a valid response.")
          get_five()
      return score

  def get_six():
      nonlocal score
      print("6. I take a positive attitude toward myself.")
      six = input("Enter D, d, a, or A: ")
      if six == "D":
          score += 0
      elif six == "d":
          score += 1
      elif six == "a":
          score += 2
      elif six == "A":
          score += 3
      else:
          print("Please enter a valid response.")
          get_six()
      return score

  def get_seven():
      nonlocal score
      print("7. On the whole, I am satisfied with myself.")
      seven = input("Enter D, d, a, or A: ")
      if seven == "D":
          score += 0
      elif seven == "d":
          score += 1
      elif seven == "a":
          score += 2
      elif seven == "A":
          score += 3
      else:
          print("Please enter a valid response.")
          get_seven()
      return score

  def get_eight():
      nonlocal score
      print("8. I wish I could have more respect for myself.")
      eight = input("Enter D, d, a, or A: ")
      if eight == "D":
          score += 3
      elif eight == "d":
          score += 2
      elif eight == "a":
          score += 1
      elif eight == "A":
          score += 0
      else:
          print("Please enter a valid response.")
          get_eight()
      return score

  def get_nine():
      nonlocal score
      print("9. I certainly feel useless at times.")
      nine = input("Enter D, d, a, or A: ")
      if nine == "D":
          score += 3
      elif nine == "d":
          score += 2
      elif nine == "a":
          score += 1
      elif nine == "A":
          score += 0
      else:
          print("Please enter a valid response.")
          get_nine()
      return score

  def get_ten():
      nonlocal score
      print("10. At times I think I am no good at all.")
      ten = input("Enter D, d, a, or A: ")
      if ten == "D":
          score += 3
      elif ten == "d":
          score += 2
      elif ten == "a":
          score += 1
      elif ten == "A":
          score += 0
      else:
          print("Please enter a valid response.")
          get_ten()
      return score


  get_one()
  get_two()
  get_three()
  get_four()
  get_five()
  get_six()
  get_seven()
  get_eight()
  get_nine()
  get_ten()

  print(f'Your score is {score}')
  if score <= 15:
      print("A score below 15 may indicate problematic low self-esteem.")

if __name__ == "__main__":
  main()