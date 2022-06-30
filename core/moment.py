from circuit_library.standard_gates.quantum_gate import QuantumGate


class Moment:
    def __init__(self,
                 *args: QuantumGate
                 ):
        """
        This is the Moment class. This is essentially a list of quantum gates that spans across quantum registers.
        For eg., consider the following poorly drawn quantum circuit

        qreg_0: |0> -- H -- X
        qreg_1: |1> -- H ----

        This circuit consists of two Moments objects m1 and m2. m1 has a list that maintains the two H gates. Whereas
        m2 has a stack that maintains X in position 0 (for qreg_0) and I (Identity Operator) in position 1.

        The contents of the lists in any two moments can be compared at any point to allow further planned optimization
        functions. The lists can be peeked to allow for reading without disturbing the alignment of the elements.

        """
        self._number_of_gates = len(args)
        self._gates = args
        self._moment_list = []

        # TODO: Initialize these values properly
        # TODO: Make sure the push method and the peek method works as expected
        # TODO: Run unit tests

    @staticmethod
    def __push_list__(self,
                      gate: QuantumGate
                      ) -> bool:
        """
        This function pushes the QuantumGate objects into the Moment list
        :param args: The actual gates that will be pushed into the Moment
        :return: True for success
        """
        # TODO: Complete this function
        return True

    def peek_list(self) -> list:
        """
        Function used to peek the list
        :param self: Peeks the current list
        :return: Returns the list held in the Moment object
        """
        # TODO: Complete this function
        return self._moment_list

    @staticmethod
    def __insert_placeholder_identity__(self,
                                        moment_list: list,
                                        ) -> bool:
        """
        Pushes a placeholder Identity Operator into the Moment list for an absent gate in order to complete a moment.
        Let's say that a QuantumCircuit object is as follows:

       qreg_0: |0> -- H -- X \n
       qreg_1: |0> ---Z ----

        We can see that the QuantumCircuit has 2 registers. qreg_0 has H gate and an X gate in sequence. ``qreg_1`` has just
        a ``Z`` gate. This means that the Moment ``m1`` will consist of ``[H,Z]`` and Moment ``m2`` will consist of [X].
        We would now want to insert a second gate ``I`` in position 1. This would complete the moment.

        In the event we have the following circuit:

        qreg_0: |0> -- H ----\n
        qreg_1: |0> ---Z --X-

        We see ``m1`` will consist of ``[H,Z]`` and ``m2`` will consist of [X]. In order to fill out the position of the identity
        operator, we will need to access the instance variables of the quantum gate (X here) and accordingly get the
        position on which it is acting on. So if X.acting_register() returns us 1, as in the case above, we shall,
        accordingly fill out Identity operators before (or after) X.acting_register.

        :param moment_list: This is the instance list variable into which the Identity operator need to be inserted into
        :return: True if success
        """

        # TODO: Extremely important method, needs to be filled out carefully!

        return True