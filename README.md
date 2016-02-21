Etc
===

Description
-----------

Etc provides some generators to give an estimated time left,
when doing big for loops in python.

Basic Usage
------------

Iterate over a range 10, returning progress and estimated time
remaining every iteration:

    for i, pi in etc.range(10):
        if pi:
            print("progress at %g"%pi.progress)
            print("%g seconds elapsed"%pi.elapsed_time)
            print("%g seconds remaining"%pi.time_remaining())
            print("")

        """
        Big task that takes a bunch of time to run
        """

Iterate over a range 100,000 returning progress info every 10 seconds:

    for i, pi in etc.range(100000, info_frequency=10):
        if pi:
            print("progress at %g"%pi.progress)
            print("%g seconds elapsed"%pi.elapsed_time)
            print("%g seconds remaining"%pi.time_remaining())
            print("")

        """
        Big task that takes a bunch of time to run
        """

Generators
----------

    etc.range(n, info_frequency=0):

Simple range from 0 to n-1 in steps of 1. More complex ranges
can be done using `sequence_timer`. Returns a tuple `(i, progress_info)`,
where `progress_info` can be either a `ProgressInfo` object, or `None`.
`info_frequency` is the time in seconds that pass between valid `progress_info`
objects getting returned from the generator.

    etc.sequence_timer(sequence, info_frequency=0):

Iterate over a sequence, such as a list. Returns a tuple `(i, progress_info)`,
where `progress_info` can be either a `ProgressInfo` object, or `None`.
`info_frequency` is the time in seconds that pass between valid `progress_info`
objects getting returned from the generator.

    etc.file_timer(in_file, info_frequency=0):

Iterate over the lines in a file. Returns a tuple `(i, progress_info)`,
where `progress_info` can be either a `ProgressInfo` object, or `None`.
`info_frequency` is the time in seconds that pass between valid `progress_info`
objects getting returned from the generator.

Classes
-------

    ProgressInfo

Information on the current progress, elapsed time, and time remaining of
the current generator.

    ProgressInfo.progress

Current progress from 0 to 1 of the generator.

    ProgressInfo.elapsed_time

Time in seconds the generator has been running.

    ProgressInfo.time_remaining()

Estimated time remaining of the loop.
