from .logs import stop_log

def novonix_tests(dash=False):
    # Further novonix tests
    with open(fileclass.name,'r') as ff:
        header = []
        fw = 'dum'
        while (fw != "[Protocol]"):
            try:
                line = ff.readline()
            except:
                log='STOP function isnovonix \n'+\
                    'REASON Reached the end of the input file \n'+\
                    '       '+str(infile)+', \n'+\
                    '       without a [Protocol] section.'
                stop_log(log,dash=dash)
                
            if line.strip():
                header.append(line) 
                fw = line.split()[0]

        # Read until the line with [Data]
        fw = 'dum'
        while (fw != "[Data]"):
            try:
                line = ff.readline()
            except:
                log='STOP function isnovonix \n'+\
                    'REASON Reached the end of the input file \n'+\
                    '       '+str(infile)+', \n'+\
                    '       without a [Data] section.'
                stop_log(log,dash=dash)
            if line.strip():
                header.append(line)
                fw = line.split()[0]

        # From the data header, read the column names
        line = ff.readline() 
        colnames = line.split(',')
        # Remove triling blancks and end of lines
        colnames = [x.strip() for x in colnames] 
        
        # Check the existance of the "Step Number" column
        if (col_step not in colnames):
            log='STOP function isnovonix \n'+\
                'REASON No "Step Number" colum found in input file \n'+\
                '       '+str(infile)
            stop_log(log,dash=dash)

        # Check the existance of the "Step time" column
        if (col_tstep not in colnames):
            log='STOP function isnovonix \n'+\
                'REASON No "Step Time" colum found in input file \n'+\
                '       '+str(infile)
            stop_log(log,dash=dash)

        # Check that the number of data columns matches the header
        line_data1 = ff.readline()
        data = line_data1.split(',')
        diff = len(data) - len(colnames)
        
        if(diff>0):
            # Add dum headers
            dums = ''
            for idiff in range(diff):
                dums = dums+',dum'+str(idiff)
                
                new_head = str(line.rstrip())+dums+' \n'
                header.append(new_head)
                
        elif(diff<0):
            log='STOP function isnovonix \n'+\
                     'REASON less data columns than header names \n'+\
                                 '       '+str(infile)
            stop_log(log,dash=dash)
        else:
            header.append(line)
            
            # Create a temporary file without blanck lines
            # and new header if needed
            tmp_file = 'tmp.csv'
            with open(tmp_file, 'w') as tf:
                for item in header:
                    tf.write(str(item))

            # Write all the data
            with open(tmp_file, 'a') as tf:
                tf.write(line_data1)
                for line in ff:
                    tf.write(line)
                    
            # Replace the input file with the new one
            move(tmp_file,infile)
    return
