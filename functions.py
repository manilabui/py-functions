# Children's activities

# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.
running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run():
		for kid in running_kids:
				print(f'{kid} was running like a fool.')

def swing():
		for kid in swinging_kids:
				print(f'{kid} swung into the night + was never seen again.')

def slide():
		for kid in sliding_kids:
				print(f'{kid} slid down the slide!')

def hide():
		for kid in hiding_kids:
				print(f'{kid} hid from the teach.')

run(), swing(), slide(), hide()