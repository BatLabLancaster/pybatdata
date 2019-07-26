import numpy as np
import pybatdata.constants as cte
def isbasytec(infile):
    """
    Given a data file, check if it exists and
    if looks like a Basytec data file

    Parameters
    ----------
    infile : string
        Name of the input Novonix data file

    Returns
    --------
    answer : boolean
        Yes=the file seems to be a Basytec data file

    Examples
    ---------
    >>> from preparenovonix.novonix_io import isnovonix
    >>> isnovonix('example_data/example_data.csv')
    True
    """

    answer = True

    # Test if the file exists
    if not os.path.isfile(infile):
        answer = False
        print(
            "STOP iobasytec.isbasytec \n"
            + "REASON Input file not found: "
            + str(infile)
            + " \n"
        )
        return answer
    else:
        with open(infile, "r") as ff:
            # Read until different header statement
            keyw = 'Basytec' 
            for line in ff:
                if line.strip():
                    char1 = line.strip()[0]
                    if char1 in cte.numberstr:
                            answer = False
                            print(
                                "STOP novonix_io.isnovonix \n"
                                + "REASON Reached the end of the input file \n"
                                + "       "
                                + str(infile)
                                + ", \n"
                                + "       without the "
                                + keyw
                                + " entry."
                            )
                            return answer
                        else:
                            if keyw in line:
                                break

            # Read until the data starts
            for line in ff:
                if line.strip():
                    char1 = line.strip()[0]
                    if char1 in nv.numberstr:
                        break
                    else:
                        last_line = line.strip()

            # From the data header, read the column names
            colnames = last_line.split(",")

            # Remove triling blancks and end of lines
            colnames = [x.strip() for x in colnames]

            # Check the existance of the "Step Number" column
            if nv.col_step not in colnames:
                answer = False
                print(
                    "STOP novonix_io.isnovonix \n"
                    + 'REASON No "Step Number" colum found in input file \n'
                    + "       "
                    + str(infile)
                    + " \n"
                )
                return answer

            # Check the existance of the "Step time" column
            if nv.col_tstep not in colnames:

                answer = False
                print(
                    "STOP novonix_io.isnovonix \n"
                    + 'REASON No "Step Time" colum found in input file \n'
                    + "       "
                    + str(infile)
                    + " \n"
                )
                return answer

    return answer
