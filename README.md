Etc
===

Description
-----------

Etc provides some generators to give an estimated time left,
when doing big for loops in python.

Generators
----------

    etc.range(n, info_frequency=0):

Simple range from 0 to n-1 in steps of 1. More complex ranges
can be done using sequence timer. Returns a tuple `(i, progress_info)`,
where `progress_info` can be either a ProgressInfo object, or None.
`info_frequency` is the time in seconds that pass between valid `progress_info`
objects getting returned from the generator.

    etc.sequence_timer(sequence, info_frequency=0):

Iterate over a sequence, such as a list. Returns a tuple `(i, progress_info)`,
where `progress_info` can be either a ProgressInfo object, or None.
`info_frequency` is the time in seconds that pass between valid `progress_info`
objects getting returned from the generator.

    etc.file_timer(in_file, info_frequency=0):

Iterate over the lines in a file. Returns a tuple `(i, progress_info)`,
where `progress_info` can be either a ProgressInfo object, or None.
`info_frequency` is the time in seconds that pass between valid `progress_info`
objects getting returned from the generator.
