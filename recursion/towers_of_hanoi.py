def tower_of_hanoi(num_disks):
    tower_of_hanoi_solution(num_disks, 's', 'a', 'd')


def tower_of_hanoi_solution(num_disks, source, auxiliary, destination):
    # easy ones
    # first: base case
    if num_disks == 0:
        return

    # second: termination condition
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return

    # move num_disks - 1 from source to auxiliary
    tower_of_hanoi_solution(num_disks - 1, source, destination, auxiliary)

    # move "leftover" / largest disk at source, to destination
    print("{} {}".format(source, destination))

    # move everything that was moved to auxiliary, to destination
    tower_of_hanoi_solution(num_disks - 1, auxiliary, source, destination)


# tower_of_hanoi(2)
tower_of_hanoi(3)
