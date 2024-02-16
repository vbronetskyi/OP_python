"""Implementation of the Polynomial ADT using a sorted linked list."""

class Polynomial:
    """Create a new polynomial object."""
    def __init__(self, degree = None, coefficient = None):
        if degree is None :
            self._poly_head = None
        else :
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    # Return the degree of the polynomial.
    def degree(self):
        """Return the degree of the polynomial"""
        if self._poly_head is None :
            return -1
        else :
            return self._poly_head.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        """Return the coefficient for the term of the given degree"""
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree >= degree :
            cur_node = cur_node.next

        if cur_node is None or cur_node.degree != degree :
            return 0.0
        else :
            return cur_node.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        """Evaluate the polynomial at the given scalar value."""
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None :
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    # Polynomial addition: newPoly = self + rhs_poly.
    def __add__(self, rhs_poly):
        """Polynomial addition: newPoly = self + rhs_poly"""
        new_poly = Polynomial()
        cur_node_self = self._poly_head
        cur_node_rhs = rhs_poly._poly_head

        while cur_node_self is not None and cur_node_rhs is not None:
            if cur_node_self.degree == cur_node_rhs.degree:
                new_coeff = cur_node_self.coefficient + cur_node_rhs.coefficient
                if new_coeff != 0:
                    new_poly._append_term(cur_node_self.degree, new_coeff)
                cur_node_self = cur_node_self.next
                cur_node_rhs = cur_node_rhs.next

            elif cur_node_self.degree > cur_node_rhs.degree:
                new_poly._append_term(cur_node_self.degree, cur_node_self.coefficient)
                cur_node_self = cur_node_self.next

            else:
                new_poly._append_term(cur_node_rhs.degree, cur_node_rhs.coefficient)
                cur_node_rhs = cur_node_rhs.next

        while cur_node_self is not None:
            new_poly._append_term(cur_node_self.degree, cur_node_self.coefficient)
            cur_node_self = cur_node_self.next

        while cur_node_rhs is not None:
            new_poly._append_term(cur_node_rhs.degree, cur_node_rhs.coefficient)
            cur_node_rhs = cur_node_rhs.next

        return new_poly

    # Polynomial subtraction: newPoly = self - rhs_poly.
    def __sub__(self, rhs_poly):
        """Polynomial subtraction: newPoly = self - rhs_poly"""
        new_poly = Polynomial()
        cur_node_self = self._poly_head
        cur_node_rhs = rhs_poly._poly_head

        while cur_node_self is not None and cur_node_rhs is not None:
            if cur_node_self.degree == cur_node_rhs.degree:
                new_coeff = cur_node_self.coefficient - cur_node_rhs.coefficient
                if new_coeff != 0:
                    new_poly._append_term(cur_node_self.degree, new_coeff)
                cur_node_self = cur_node_self.next
                cur_node_rhs = cur_node_rhs.next

            elif cur_node_self.degree > cur_node_rhs.degree:
                new_poly._append_term(cur_node_self.degree, cur_node_self.coefficient)
                cur_node_self = cur_node_self.next

            else:
                new_poly._append_term(cur_node_rhs.degree, -cur_node_rhs.coefficient)
                cur_node_rhs = cur_node_rhs.next

        while cur_node_self is not None:
            new_poly._append_term(cur_node_self.degree, cur_node_self.coefficient)
            cur_node_self = cur_node_self.next

        while cur_node_rhs is not None:
            new_poly._append_term(cur_node_rhs.degree, -cur_node_rhs.coefficient)
            cur_node_rhs = cur_node_rhs.next

        return new_poly

    # Polynomial multiplication: newPoly = self * rhs_poly.
    def __mul__(self, rhs_poly):
        """Polynomial multiplication: newPoly = self * rhs_poly."""
        new_poly = Polynomial()
        cur_node_rhs = rhs_poly._poly_head

        while cur_node_rhs is not None:
            new_sub_poly = Polynomial()
            cur_node_self = self._poly_head

            while cur_node_self is not None:
                new_degree = cur_node_self.degree + cur_node_rhs.degree
                new_coeff = cur_node_self.coefficient * cur_node_rhs.coefficient
                new_sub_poly._append_term(new_degree, new_coeff)
                cur_node_self = cur_node_self.next

            new_poly += new_sub_poly
            cur_node_rhs = cur_node_rhs.next

        return new_poly


    def simple_add(self, rhs_poly):
        """simple_add method"""
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_megree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            value = self[i] + rhs_poly[i]
            new_poly._append_term(i, value)
            i += 1
        return new_poly

    # Helper method for appending terms to the polynomial.
    def _append_term(self, degree, coefficient):
        """Helper method for appending terms to the polynomial."""
        if coefficient != 0.0:
            new_term =_PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x" + str(self.degree)
