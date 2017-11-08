# This is a repository for parts of code I have written but
# have not implemented or lack the supporting code they require

# Define the global variable lists for Prosecution scores

p_open_raw = []
pa_dir1_raw = []
pw_dir1_raw = []
pw_crs1_raw = []
pa_dir2_raw = []
pw_dir2_raw = []
pw_crs2_raw = []
pa_dir3_raw = []
pw_dir3_raw = []
pw_crs3_raw = []
pa_cross1_raw = []
pa_cross2_raw = []
pa_cross3_raw = []
p_close_raw = []
pa_dir_avg = []
pw_dir_avg = []

# Define the global variable lists for Defense scores

d_open_raw = []
da_cross1_raw = []
da_cross2_raw = []
da_cross3_raw = []
da_dir1_raw = []
dw_dir1_raw = []
dw_crs1_raw = []
da_dir2_raw = []
dw_dir2_raw = []
dw_crs2_raw = []
da_dir3_raw = []
dw_dir3_raw = []
dw_crs3_raw = []
d_close_raw = []
da_dir_avg = []
dw_dir_avg = []

# Function saves results to the appropriate arrays and makes all results int

    def save(self):
        self.pa_dir_avg = (int(self.pa_dir1_raw.get()) + int(self.pa_dir2_raw.get()) + int(self.pa_dir3_raw.get())) / 3
        self.pw_dir_avg = (int(self.pw_dir1_raw.get()) + int(self.pw_dir2_raw.get()) + int(self.pw_dir3_raw.get())) / 3
        self.da_dir_avg = (int(self.da_dir1_raw.get()) + int(self.da_dir2_raw.get()) + int(self.da_dir3_raw.get())) / 3
        self.dw_dir_avg = (int(self.dw_dir1_raw.get()) + int(self.dw_dir2_raw.get()) + int(self.dw_dir3_raw.get())) / 3
        p_open_raw.insert((int(self.ballot_num.get()) - 1), int(self.p_open_raw.get()))
        pa_dir1_raw.insert((int(self.ballot_num.get()) - 1), int(self.pa_dir1_raw.get()))
        pw_dir1_raw.insert((int(self.ballot_num.get()) - 1), int(self.pw_dir1_raw.get()))
        pw_crs1_raw.insert((int(self.ballot_num.get()) - 1), int(self.pw_crs1_raw.get()))
        pa_dir2_raw.insert((int(self.ballot_num.get()) - 1), int(self.pa_dir2_raw.get()))
        pw_dir2_raw.insert((int(self.ballot_num.get()) - 1), int(self.pw_dir2_raw.get()))
        pw_crs2_raw.insert((int(self.ballot_num.get()) - 1), int(self.pw_crs2_raw.get()))
        pa_dir3_raw.insert((int(self.ballot_num.get()) - 1), int(self.pa_dir3_raw.get()))
        pw_dir3_raw.insert((int(self.ballot_num.get()) - 1), int(self.pw_dir3_raw.get()))
        pw_crs3_raw.insert((int(self.ballot_num.get()) - 1), int(self.pw_crs3_raw.get()))
        pa_cross1_raw.insert((int(self.ballot_num.get()) - 1), int(self.pa_cross1_raw.get()))
        pa_cross2_raw.insert((int(self.ballot_num.get()) - 1), int(self.pa_cross2_raw.get()))
        pa_cross3_raw.insert((int(self.ballot_num.get()) - 1), int(self.pa_cross3_raw.get()))
        p_close_raw.insert((int(self.ballot_num.get()) - 1), int(self.p_close_raw.get()))
        pa_dir_avg.insert((int(self.ballot_num.get()) - 1), self.pa_dir_avg)
        pw_dir_avg.insert((int(self.ballot_num.get()) - 1), self.pw_dir_avg)
        d_open_raw.insert((int(self.ballot_num.get()) - 1), int(self.d_open_raw.get()))
        da_cross1_raw.insert((int(self.ballot_num.get()) - 1), int(self.da_cross1_raw.get()))
        da_cross2_raw.insert((int(self.ballot_num.get()) - 1), int(self.da_cross2_raw.get()))
        da_cross3_raw.insert((int(self.ballot_num.get()) - 1), int(self.da_cross3_raw.get()))
        da_dir1_raw.insert((int(self.ballot_num.get()) - 1), int(self.da_dir1_raw.get()))
        dw_dir1_raw.insert((int(self.ballot_num.get()) - 1), int(self.dw_dir1_raw.get()))
        dw_crs1_raw.insert((int(self.ballot_num.get()) - 1), int(self.dw_crs1_raw.get()))
        da_dir2_raw.insert((int(self.ballot_num.get()) - 1), int(self.da_dir2_raw.get()))
        dw_dir2_raw.insert((int(self.ballot_num.get()) - 1), int(self.dw_dir2_raw.get()))
        dw_crs2_raw.insert((int(self.ballot_num.get()) - 1), int(self.dw_crs2_raw.get()))
        da_dir3_raw.insert((int(self.ballot_num.get()) - 1), int(self.da_dir3_raw.get()))
        dw_dir3_raw.insert((int(self.ballot_num.get()) - 1), int(self.dw_dir3_raw.get()))
        dw_crs3_raw.insert((int(self.ballot_num.get()) - 1), int(self.dw_crs3_raw.get()))
        d_close_raw.insert((int(self.ballot_num.get()) - 1), int(self.d_close_raw.get()))
        da_dir_avg.insert((int(self.ballot_num.get()) - 1), self.da_dir_avg)
        dw_dir_avg.insert((int(self.ballot_num.get()) - 1), self.dw_dir_avg)
