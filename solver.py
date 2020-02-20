# Python Template for Google Hash Code Challenge
# Replace all TODOS and profit. Good Luck

def main():
    problem_files = ['problem1.txt'] # TODO replace with actual inputs
    for problem_file in problem_files:
        print('Parsing problem ' + problem_file)
        problem = parse_input(problem_file)
        print('Solving problem ' + problem_file)
        solution = problem.solve()
        solution.to_file('solution_' + problem_file)


class Problem:
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return str(self.info)

    def solve(self):
        # TODO Solve the problem here :)
        self.info = self.info + 1
        return Solution(self.info)


class Solution:
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return str(self.info)

    def to_file(self, file_name):
        file_name = 'output/' + file_name
        file = open(file_name, 'w')
        # TODO Define the format of the Output file
        file.write(str(self.info))
        file.write('\n')
        file.close()


def parse_input(file_name):
    num = 0
    for line in open('input/'+file_name):
        # TODO Parse Problem File here
        num += safe_cast(line, int, 0)
    return Problem(num)


def safe_cast(val, to_type, default=None):
    '''
    Cast value. In case of error, return default.
    '''
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

if __name__ == "__main__":
    main()
