#!/usr/bin/python
from tkinter import Tk, Label, Button, Entry, END
import os


class Ballot:
    def __init__(self, master):
        self.master = master
        master.title("Enter ballot results")

# Define the ballot number label and entry field

        self.label_tour_name = Label(master, text="Tournament Name")
        self.label_tour_name.grid(row=1, column=1)

        self.tour_name = Entry(master)
        self.tour_name.grid(row=1, column=2)

# Define the ballot number label and entry field

        self.label_ballot_num = Label(master, text="Ballot #")
        self.label_ballot_num.grid(row=1, column=3)

        self.ballot_num = Entry(master)
        self.ballot_num.grid(row=1, column=4)

# Define the description label and entry field

        self.label_ballot_des = Label(master, text="Ballot Description")
        self.label_ballot_des.grid(row=1, column=5)

        self.ballot_des = Entry(master)
        self.ballot_des.grid(row=1, column=6)

# Define side labels

        self.label_p_side = Label(master, text="π")
        self.label_p_side.grid(row=2, column=2)

        self.label_d_side = Label(master, text="Δ")
        self.label_d_side.grid(row=2, column=5)

# Define Prosecution open label and entry field

        self.label_p_open = Label(master, text="π Opening")
        self.label_p_open.grid(row=3, column=1)

        self.p_open_raw = Entry(master)
        self.p_open_raw.grid(row=3, column=2)

# Define Defense open label and entry field

        self.label_d_open = Label(master, text="Δ Opening")
        self.label_d_open.grid(row=3, column=5)

        self.d_open_raw = Entry(master)
        self.d_open_raw.grid(row=3, column=6)

# Define Prosecution case in chief label

        self.label_p_case = Label(master, text="π Case in Chief")
        self.label_p_case.grid(row=4, column=3, columnspan=2)

# Define Prosecution direct 1 label and entry field for attorney

        self.label_pa_dir1 = Label(master, text="π Attorney - Direct 1")
        self.label_pa_dir1.grid(row=5, column=1)

        self.pa_dir1_raw = Entry(master)
        self.pa_dir1_raw.grid(row=5, column=2)

# Define Defense cross 1 label and entry field for attorney

        self.label_da_cross1 = Label(master, text="Δ Attorney - Cross 1")
        self.label_da_cross1.grid(row=5, column=5)

        self.da_cross1_raw = Entry(master)
        self.da_cross1_raw.grid(row=5, column=6)

# Define Prosecution direct 1 label and entry field for witness

        self.label_pw_dir1 = Label(master, text="π Witness - Direct 1")
        self.label_pw_dir1.grid(row=6, column=1)

        self.pw_dir1_raw = Entry(master)
        self.pw_dir1_raw.grid(row=6, column=2)

# Define Prosecution cross 1 label and entry field for witness

        self.label_pw_crs1 = Label(master, text="π Witness - Cross 1")
        self.label_pw_crs1.grid(row=7, column=1)

        self.pw_crs1_raw = Entry(master)
        self.pw_crs1_raw.grid(row=7, column=2)

# Define Prosecution direct 2 label and entry field for attorney

        self.label_pa_dir2 = Label(master, text="π Attorney - Direct 2")
        self.label_pa_dir2.grid(row=8, column=1)

        self.pa_dir2_raw = Entry(master)
        self.pa_dir2_raw.grid(row=8, column=2)

# Define Defense cross 2 label and entry field for attorney

        self.label_da_cross2 = Label(master, text="Δ Attorney - Cross 2")
        self.label_da_cross2.grid(row=8, column=5)

        self.da_cross2_raw = Entry(master)
        self.da_cross2_raw.grid(row=8, column=6)

# Define Prosecution direct 2 label and entry field for witness

        self.label_pw_dir2 = Label(master, text="π Witness - Direct 2")
        self.label_pw_dir2.grid(row=9, column=1)

        self.pw_dir2_raw = Entry(master)
        self.pw_dir2_raw.grid(row=9, column=2)

# Define Prosecution cross 2 label and entry field for witness

        self.label_pw_crs2 = Label(master, text="π Witness - Cross 2")
        self.label_pw_crs2.grid(row=10, column=1)

        self.pw_crs2_raw = Entry(master)
        self.pw_crs2_raw.grid(row=10, column=2)

# Define Prosecution direct 3 label and entry field for attorney

        self.label_pa_dir3 = Label(master, text="π Attorney - Direct 3")
        self.label_pa_dir3.grid(row=11, column=1)

        self.pa_dir3_raw = Entry(master)
        self.pa_dir3_raw.grid(row=11, column=2)

# Define Defense cross 3 label and entry field for attorney

        self.label_da_cross3 = Label(master, text="Δ Attorney - Cross 3")
        self.label_da_cross3.grid(row=11, column=5)

        self.da_cross3_raw = Entry(master)
        self.da_cross3_raw.grid(row=11, column=6)

# Define Prosecution direct 3 label and entry field for witness

        self.label_pw_dir3 = Label(master, text="π Witness - Direct 3")
        self.label_pw_dir3.grid(row=12, column=1)

        self.pw_dir3_raw = Entry(master)
        self.pw_dir3_raw.grid(row=12, column=2)

# Define Prosecution cross 3 label and entry field for witness

        self.label_pw_crs3 = Label(master, text="π Witness - Cross 3")
        self.label_pw_crs3.grid(row=13, column=1)

        self.pw_crs3_raw = Entry(master)
        self.pw_crs3_raw.grid(row=13, column=2)

# Define Defense case in chief label

        self.label_p_case = Label(master, text="Δ Case in Chief")
        self.label_p_case.grid(row=14, column=3, columnspan=2)

# Define Prosecution cross 1 label and entry field for attorney

        self.label_pa_cross1 = Label(master, text="π Attorney - Cross 1")
        self.label_pa_cross1.grid(row=15, column=1)

        self.pa_cross1_raw = Entry(master)
        self.pa_cross1_raw.grid(row=15, column=2)

# Define Defense direct 1 label and entry field for attorney

        self.label_da_dir1 = Label(master, text="Δ Attorney - Direct 1")
        self.label_da_dir1.grid(row=15, column=5)

        self.da_dir1_raw = Entry(master)
        self.da_dir1_raw.grid(row=15, column=6)

# Define Defense direct 1 label and entry field for witness

        self.label_dw_dir1 = Label(master, text="Δ Witness - Direct 1")
        self.label_dw_dir1.grid(row=16, column=5)

        self.dw_dir1_raw = Entry(master)
        self.dw_dir1_raw.grid(row=16, column=6)

# Define Defense cross 1 label and entry field for witness

        self.label_dw_crs1 = Label(master, text="Δ Witness - Cross 1")
        self.label_dw_crs1.grid(row=17, column=5)

        self.dw_crs1_raw = Entry(master)
        self.dw_crs1_raw.grid(row=17, column=6)

# Define Prosecution cross 2 label and entry field for attorney

        self.label_pa_cross2 = Label(master, text="π Attorney - Cross 2")
        self.label_pa_cross2.grid(row=18, column=1)

        self.pa_cross2_raw = Entry(master)
        self.pa_cross2_raw.grid(row=18, column=2)

# Define Defense direct 2 label and entry field for attorney

        self.label_da_dir2 = Label(master, text="Δ Attorney - Direct 2")
        self.label_da_dir2.grid(row=18, column=5)

        self.da_dir2_raw = Entry(master)
        self.da_dir2_raw.grid(row=18, column=6)

# Define Defense direct 2 label and entry field for witness

        self.label_dw_dir2 = Label(master, text="Δ Witness - Direct 2")
        self.label_dw_dir2.grid(row=19, column=5)

        self.dw_dir2_raw = Entry(master)
        self.dw_dir2_raw.grid(row=19, column=6)

# Define Defense cross 2 label and entry field for witness

        self.label_dw_crs2 = Label(master, text="Δ Witness - Cross 2")
        self.label_dw_crs2.grid(row=20, column=5)

        self.dw_crs2_raw = Entry(master)
        self.dw_crs2_raw.grid(row=20, column=6)

# Define Prosecution cross 3 label and entry field for attorney

        self.label_pa_cross3 = Label(master, text="π Attorney - Cross 3")
        self.label_pa_cross3.grid(row=21, column=1)

        self.pa_cross3_raw = Entry(master)
        self.pa_cross3_raw.grid(row=21, column=2)

# Define Defense direct 3 label and entry field for attorney

        self.label_da_dir3 = Label(master, text="Δ Attorney - Direct 3")
        self.label_da_dir3.grid(row=21, column=5)

        self.da_dir3_raw = Entry(master)
        self.da_dir3_raw.grid(row=21, column=6)

# Define Defense direct 3 label and entry field for witness

        self.label_dw_dir3 = Label(master, text="Δ Witness - Direct 3")
        self.label_dw_dir3.grid(row=22, column=5)

        self.dw_dir3_raw = Entry(master)
        self.dw_dir3_raw.grid(row=22, column=6)

# Define Defense cross 3 label and entry field for witness

        self.label_dw_crs3 = Label(master, text="Δ Witness - Cross 3")
        self.label_dw_crs3.grid(row=23, column=5)

        self.dw_crs3_raw = Entry(master)
        self.dw_crs3_raw.grid(row=23, column=6)

# Define Closing label and fill some space to better space grid

        self.label_close = Label(master, text="Closings")
        self.label_close.grid(row=24, column=3, columnspan=2)

# Define Prosecution close label and entry field

        self.label_p_close = Label(master, text="π Closing")
        self.label_p_close.grid(row=25, column=1)

        self.p_close_raw = Entry(master)
        self.p_close_raw.grid(row=25, column=2)

# Define Defense close label and entry field

        self.label_d_close = Label(master, text="Δ Closing")
        self.label_d_close.grid(row=25, column=5)

        self.d_close_raw = Entry(master)
        self.d_close_raw.grid(row=25, column=6)

# Add whitespace between closings and buttons

        self.label_endspace = Label(master, text=" ")
        self.label_endspace.grid(row=26, column=3, columnspan=2)

# Define the buttons

        self.button_save_ballot = Button(master, text="Save", command=self.save)  # noqa
        self.button_save_ballot.grid(row=27, column=2)

        self.button_close = Button(master, text="Close", command=master.quit)
        self.button_close.grid(row=27, column=5)

        self.button_clear = Button(master, text="Clear Text", command=self.clear)  # noqa
        self.button_clear.grid(row=27, column=3, columnspan=2)

# Function tests the save button by printing the global variables

    def clear(self):

        self.ballot_num.delete(0, END)
        self.ballot_des.delete(0, END)
        self.p_open_raw.delete(0, END)
        self.pa_dir1_raw.delete(0, END)
        self.pw_dir1_raw.delete(0, END)
        self.pw_crs1_raw.delete(0, END)
        self.pa_dir2_raw.delete(0, END)
        self.pw_dir2_raw.delete(0, END)
        self.pw_crs2_raw.delete(0, END)
        self.pa_dir3_raw.delete(0, END)
        self.pw_dir3_raw.delete(0, END)
        self.pw_crs3_raw.delete(0, END)
        self.pa_cross1_raw.delete(0, END)
        self.pa_cross2_raw.delete(0, END)
        self.pa_cross3_raw.delete(0, END)
        self.p_close_raw.delete(0, END)
        self.d_open_raw.delete(0, END)
        self.da_cross1_raw.delete(0, END)
        self.da_cross2_raw.delete(0, END)
        self.da_cross3_raw.delete(0, END)
        self.da_dir1_raw.delete(0, END)
        self.dw_dir1_raw.delete(0, END)
        self.dw_crs1_raw.delete(0, END)
        self.da_dir2_raw.delete(0, END)
        self.dw_dir2_raw.delete(0, END)
        self.dw_crs2_raw.delete(0, END)
        self.da_dir3_raw.delete(0, END)
        self.dw_dir3_raw.delete(0, END)
        self.dw_crs3_raw.delete(0, END)
        self.d_close_raw.delete(0, END)

# Function saves results to the appropriate arrays and makes all results int

    def save(self):
        if not self.ballot_des.get():
            file_name = self.tour_name.get() + "-" + self.ballot_num.get()
            + ".ballot"
        else:
            file_name = self.tour_name.get() + "-" + self.ballot_num.get()
            + "(" + self.ballot_des + ").ballot"
        self.pa_dir_avg = (int(self.pa_dir1_raw.get())
                           + int(self.pa_dir2_raw.get())
                           + int(self.pa_dir3_raw.get())) / 3
        self.pw_dir_avg = (int(self.pw_dir1_raw.get())
                           + int(self.pw_dir2_raw.get())
                           + int(self.pw_dir3_raw.get())) / 3
        self.da_dir_avg = (int(self.da_dir1_raw.get())
                           + int(self.da_dir2_raw.get())
                           + int(self.da_dir3_raw.get())) / 3
        self.dw_dir_avg = (int(self.dw_dir1_raw.get())
                           + int(self.dw_dir2_raw.get())
                           + int(self.dw_dir3_raw.get())) / 3
#        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(os.path.join(os.path.expanduser('~'),
                  'Documents', 'BallotRW', file_name), "w") as ballot:
            ballot.write(self.p_open_raw.get())
            ballot.write(":")
            ballot.write(self.pa_dir1_raw.get())
            ballot.write(":")
            ballot.write(self.pw_dir1_raw.get())
            ballot.write(":")
            ballot.write(self.pw_crs1_raw.get())
            ballot.write(":")
            ballot.write(self.pa_dir2_raw.get())
            ballot.write(":")
            ballot.write(self.pw_dir2_raw.get())
            ballot.write(":")
            ballot.write(self.pw_crs2_raw.get())
            ballot.write(":")
            ballot.write(self.pa_dir3_raw.get())
            ballot.write(":")
            ballot.write(self.pw_dir3_raw.get())
            ballot.write(":")
            ballot.write(self.pw_crs3_raw.get())
            ballot.write(":")
            ballot.write(self.pa_cross1_raw.get())
            ballot.write(":")
            ballot.write(self.pa_cross2_raw.get())
            ballot.write(":")
            ballot.write(self.pa_cross3_raw.get())
            ballot.write(":")
            ballot.write(self.p_close_raw.get())
            ballot.write(":")
            ballot.write(self.d_open_raw.get())
            ballot.write(":")
            ballot.write(self.da_cross1_raw.get())
            ballot.write(":")
            ballot.write(self.da_cross2_raw.get())
            ballot.write(":")
            ballot.write(self.da_cross3_raw.get())
            ballot.write(":")
            ballot.write(self.da_dir1_raw.get())
            ballot.write(":")
            ballot.write(self.dw_dir1_raw.get())
            ballot.write(":")
            ballot.write(self.dw_crs1_raw.get())
            ballot.write(":")
            ballot.write(self.da_dir2_raw.get())
            ballot.write(":")
            ballot.write(self.dw_dir2_raw.get())
            ballot.write(":")
            ballot.write(self.dw_crs2_raw.get())
            ballot.write(":")
            ballot.write(self.da_dir3_raw.get())
            ballot.write(":")
            ballot.write(self.dw_dir3_raw.get())
            ballot.write(":")
            ballot.write(self.dw_crs3_raw.get())
            ballot.write(":")
            ballot.write(self.d_close_raw.get())
            ballot.write(":")
            ballot.write(str(self.pa_dir_avg))
            ballot.write(":")
            ballot.write(str(self.pw_dir_avg))
            ballot.write(":")
            ballot.write(str(self.da_dir_avg))
            ballot.write(":")
            ballot.write(str(self.dw_dir_avg))
            ballot.write(":")


class Roles:
    def __init__(self, master):
        self.master = master
        master.title("Choose your roles for this ballot")

# Define the ballot number label and entry field

        self.label_ballot_num = Label(master, text="Ballot #")
        self.label_ballot_num.grid(row=1, column=3)

        self.ballot_num_sel = Label(master, text="1")
        self.ballot_num_sel.grid(row=1, column=4)

# Define side labels

        self.label_p_side = Label(master, text="π")
        self.label_p_side.grid(row=2, column=2)

        self.label_d_side = Label(master, text="Δ")
        self.label_d_side.grid(row=2, column=5)

# Define Prosecution open label and entry field

        self.label_p_open = Label(master, text="π Opening")
        self.label_p_open.grid(row=3, column=1)

        self.p_open_raw = Entry(master)
        self.p_open_raw.grid(row=3, column=2)

# Define Defense open label and entry field

        self.label_d_open = Label(master, text="Δ Opening")
        self.label_d_open.grid(row=3, column=5)

        self.d_open_raw = Entry(master)
        self.d_open_raw.grid(row=3, column=6)

# Define Prosecution case in chief label

        self.label_p_case = Label(master, text="π Case in Chief")
        self.label_p_case.grid(row=4, column=3, columnspan=2)

# Define Prosecution direct 1 label and entry field for attorney

        self.label_pa_dir1 = Label(master, text="π Attorney - Direct 1")
        self.label_pa_dir1.grid(row=5, column=1)

        self.pa_dir1_raw = Entry(master)
        self.pa_dir1_raw.grid(row=5, column=2)

# Define Defense cross 1 label and entry field for attorney

        self.label_da_cross1 = Label(master, text="Δ Attorney - Cross 1")
        self.label_da_cross1.grid(row=5, column=5)

        self.da_cross1_raw = Entry(master)
        self.da_cross1_raw.grid(row=5, column=6)

# Define Prosecution direct 1 label and entry field for witness

        self.label_pw_dir1 = Label(master, text="π Witness - Direct 1")
        self.label_pw_dir1.grid(row=6, column=1)

        self.pw_dir1_raw = Entry(master)
        self.pw_dir1_raw.grid(row=6, column=2)

# Define Prosecution cross 1 label and entry field for witness

        self.label_pw_crs1 = Label(master, text="π Witness - Cross 1")
        self.label_pw_crs1.grid(row=7, column=1)

        self.pw_crs1_raw = Entry(master)
        self.pw_crs1_raw.grid(row=7, column=2)

# Define Prosecution direct 2 label and entry field for attorney

        self.label_pa_dir2 = Label(master, text="π Attorney - Direct 2")
        self.label_pa_dir2.grid(row=8, column=1)

        self.pa_dir2_raw = Entry(master)
        self.pa_dir2_raw.grid(row=8, column=2)

# Define Defense cross 2 label and entry field for attorney

        self.label_da_cross2 = Label(master, text="Δ Attorney - Cross 2")
        self.label_da_cross2.grid(row=8, column=5)

        self.da_cross2_raw = Entry(master)
        self.da_cross2_raw.grid(row=8, column=6)

# Define Prosecution direct 2 label and entry field for witness

        self.label_pw_dir2 = Label(master, text="π Witness - Direct 2")
        self.label_pw_dir2.grid(row=9, column=1)

        self.pw_dir2_raw = Entry(master)
        self.pw_dir2_raw.grid(row=9, column=2)

# Define Prosecution cross 2 label and entry field for witness

        self.label_pw_crs2 = Label(master, text="π Witness - Cross 2")
        self.label_pw_crs2.grid(row=10, column=1)

        self.pw_crs2_raw = Entry(master)
        self.pw_crs2_raw.grid(row=10, column=2)

# Define Prosecution direct 3 label and entry field for attorney

        self.label_pa_dir3 = Label(master, text="π Attorney - Direct 3")
        self.label_pa_dir3.grid(row=11, column=1)

        self.pa_dir3_raw = Entry(master)
        self.pa_dir3_raw.grid(row=11, column=2)

# Define Defense cross 3 label and entry field for attorney

        self.label_da_cross3 = Label(master, text="Δ Attorney - Cross 3")
        self.label_da_cross3.grid(row=11, column=5)

        self.da_cross3_raw = Entry(master)
        self.da_cross3_raw.grid(row=11, column=6)

# Define Prosecution direct 3 label and entry field for witness

        self.label_pw_dir3 = Label(master, text="π Witness - Direct 3")
        self.label_pw_dir3.grid(row=12, column=1)

        self.pw_dir3_raw = Entry(master)
        self.pw_dir3_raw.grid(row=12, column=2)

# Define Prosecution cross 3 label and entry field for witness

        self.label_pw_crs3 = Label(master, text="π Witness - Cross 3")
        self.label_pw_crs3.grid(row=13, column=1)

        self.pw_crs3_raw = Entry(master)
        self.pw_crs3_raw.grid(row=13, column=2)

# Define Defense case in chief label

        self.label_p_case = Label(master, text="Δ Case in Chief")
        self.label_p_case.grid(row=14, column=3, columnspan=2)

# Define Prosecution cross 1 label and entry field for attorney

        self.label_pa_cross1 = Label(master, text="π Attorney - Cross 1")
        self.label_pa_cross1.grid(row=15, column=1)

        self.pa_cross1_raw = Entry(master)
        self.pa_cross1_raw.grid(row=15, column=2)

# Define Defense direct 1 label and entry field for attorney

        self.label_da_dir1 = Label(master, text="Δ Attorney - Direct 1")
        self.label_da_dir1.grid(row=15, column=5)

        self.da_dir1_raw = Entry(master)
        self.da_dir1_raw.grid(row=15, column=6)

# Define Defense direct 1 label and entry field for witness

        self.label_dw_dir1 = Label(master, text="Δ Witness - Direct 1")
        self.label_dw_dir1.grid(row=16, column=5)

        self.dw_dir1_raw = Entry(master)
        self.dw_dir1_raw.grid(row=16, column=6)

# Define Defense cross 1 label and entry field for witness

        self.label_dw_crs1 = Label(master, text="Δ Witness - Cross 1")
        self.label_dw_crs1.grid(row=17, column=5)

        self.dw_crs1_raw = Entry(master)
        self.dw_crs1_raw.grid(row=17, column=6)

# Define Prosecution cross 2 label and entry field for attorney

        self.label_pa_cross2 = Label(master, text="π Attorney - Cross 2")
        self.label_pa_cross2.grid(row=18, column=1)

        self.pa_cross2_raw = Entry(master)
        self.pa_cross2_raw.grid(row=18, column=2)

# Define Defense direct 2 label and entry field for attorney

        self.label_da_dir2 = Label(master, text="Δ Attorney - Direct 2")
        self.label_da_dir2.grid(row=18, column=5)

        self.da_dir2_raw = Entry(master)
        self.da_dir2_raw.grid(row=18, column=6)

# Define Defense direct 2 label and entry field for witness

        self.label_dw_dir2 = Label(master, text="Δ Witness - Direct 2")
        self.label_dw_dir2.grid(row=19, column=5)

        self.dw_dir2_raw = Entry(master)
        self.dw_dir2_raw.grid(row=19, column=6)

# Define Defense cross 2 label and entry field for witness

        self.label_dw_crs2 = Label(master, text="Δ Witness - Cross 2")
        self.label_dw_crs2.grid(row=20, column=5)

        self.dw_crs2_raw = Entry(master)
        self.dw_crs2_raw.grid(row=20, column=6)

# Define Prosecution cross 3 label and entry field for attorney

        self.label_pa_cross3 = Label(master, text="π Attorney - Cross 3")
        self.label_pa_cross3.grid(row=21, column=1)

        self.pa_cross3_raw = Entry(master)
        self.pa_cross3_raw.grid(row=21, column=2)

# Define Defense direct 3 label and entry field for attorney

        self.label_da_dir3 = Label(master, text="Δ Attorney - Direct 3")
        self.label_da_dir3.grid(row=21, column=5)

        self.da_dir3_raw = Entry(master)
        self.da_dir3_raw.grid(row=21, column=6)

# Define Defense direct 3 label and entry field for witness

        self.label_dw_dir3 = Label(master, text="Δ Witness - Direct 3")
        self.label_dw_dir3.grid(row=22, column=5)

        self.dw_dir3_raw = Entry(master)
        self.dw_dir3_raw.grid(row=22, column=6)

# Define Defense cross 3 label and entry field for witness

        self.label_dw_crs3 = Label(master, text="Δ Witness - Cross 3")
        self.label_dw_crs3.grid(row=23, column=5)

        self.dw_crs3_raw = Entry(master)
        self.dw_crs3_raw.grid(row=23, column=6)

# Define Closing label and fill some space to better space grid

        self.label_close = Label(master, text="Closings")
        self.label_close.grid(row=24, column=3, columnspan=2)

# Define Prosecution close label and entry field

        self.label_p_close = Label(master, text="π Closing")
        self.label_p_close.grid(row=25, column=1)

        self.p_close_raw = Entry(master)
        self.p_close_raw.grid(row=25, column=2)

# Define Defense close label and entry field

        self.label_d_close = Label(master, text="Δ Closing")
        self.label_d_close.grid(row=25, column=5)

        self.d_close_raw = Entry(master)
        self.d_close_raw.grid(row=25, column=6)

# Add whitespace between closings and buttons

        self.label_endspace = Label(master, text=" ")
        self.label_endspace.grid(row=26, column=3, columnspan=2)

# Define the buttons

        self.button_save_ballot = Button(master, text="Print", command=self.save)  # noqa
        self.button_save_ballot.grid(row=27, column=2)

        self.button_close = Button(master, text="Close", command=master.quit)
        self.button_close.grid(row=27, column=5)

# Function will eventually save results to array, now just prints ballot_num

    def save(self):
        print(self.ballot_num.get())


root = Tk()
ballot = Ballot(root)
root.mainloop()
