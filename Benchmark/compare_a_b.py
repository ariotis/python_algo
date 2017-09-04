import timeit


class Compare(object):
    def __init__(self, a, b):
        """
        Initialize with two functions.  These will be called and compared with
        assertions and run times to contrast their differences.

        """

        self.a = a
        self.a_name = self.a.__name__

        self.b = b
        self.b_name = self.b.__name__

    def __repr__(self):
        """
        Print out all tests in a nicely formatted statement.
        :return: string of all tests, formatted.
        """
        run_times_results = self.run_times()

        formatted_response = """
        Comparing {a_name} to {b_name}...
        {a_name} ran in {a_time} seconds.
        {b_name} ran in {b_time} seconds.
        
        {winner} was faster by {diff} seconds, which was {factor} times faster.
        """.format(
            a_name=self.a_name,
            b_name=self.b_name,
            a_time=run_times_results[self.a_name],
            b_time=run_times_results[self.b_name],
            diff=run_times_results['difference'],
            winner=run_times_results['winner'],
            factor=self.__times_faster(run_times_results[self.a_name],
                                       run_times_results[self.b_name])
        )

        return formatted_response

    def __winner(self, a_run_time, b_run_time):
        if a_run_time == b_run_time:
            winner = 'tie'
        elif a_run_time < b_run_time:
            winner = self.a_name
        else:
            winner = self.b_name

        return winner

    @staticmethod
    def __difference(a_run_time, b_run_time):
        return max(a_run_time, b_run_time) - min(a_run_time, b_run_time)

    @staticmethod
    def __times_faster(a_time, b_time):
        """
        Calculates the multiplier (rounded to 2 decimal points) that the run
        times differ by.
        :param a_time: a float of a run time
        :param b_time: a float of b run time
        :return: float (rounded 2 decimal points) of the multiplier difference
        """

        return round(min(a_time, b_time) / max(a_time, b_time),2)

    def run_times(self):
        """
        Run self.a and compare runtime to self.b.
        :return: a dict of A run time, B run time, the difference, and the
        winner.
        """

        # Initialize timeit strings
        import_template = "from __main__ import {name}"
        stmt_template = "{name}()"

        a_timeit_import = import_template.format(name=self.a_name)
        b_timeit_import = import_template.format(name=self.b_name)

        a_stmt = stmt_template.format(name=self.a_name)
        b_stmt = stmt_template.format(name=self.b_name)

        a_run_time = timeit.Timer(setup=a_timeit_import, stmt=a_stmt).timeit()
        b_run_time = timeit.Timer(setup=b_timeit_import, stmt=b_stmt).timeit()

        return {self.a_name: a_run_time,
                self.b_name: b_run_time,
                'difference': self.__difference(a_run_time, b_run_time),
                'winner': self.__winner(a_run_time, b_run_time)}

    def print_results(self):
        return print(self.__repr__())