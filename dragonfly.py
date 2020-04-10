"""
Initialize the dragonflies population Xi (i = 1, 2, ..., n)
Initialize step vectors ΔXi (i = 1, 2, ..., n)
while the end condition is not satisfied
       Calculate the objective values of all dragonflies
       Update the food source and enemy
       Update w, s, a, c, f, and e
       Calculate S, A, C, F, and E using Eqs. (3.1) to (3.5) in the paper (or above the page)
       Update neighbouring radius
       if a dragonfly has at least one  neighbouring dragonfly
               Update velocity vector using Eq. (3.6) in the paper (or above the page)
               Update position vector using Eq. (3.7) in the paper (or above the page)
       else
               Update position vector using Eq. (3.8) in the paper (or above the page)
       end if
       Check and correct the new positions based on the boundaries of variables
end while
"""