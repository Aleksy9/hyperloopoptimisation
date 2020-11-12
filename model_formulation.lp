\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  2 pax_1_2 + 2 pax_2_3 + 5 pax_3_1 - 2 x_1_2 - 5 x_2_3 - 5 x_3_1 - nt_1_2
   - nt_2_3 - nt_3_1 - 2 nv_1_2 - 2 nv_2_3 - 2 nv_3_1
Subject To
 max_tubes_1_2: - 2 x_1_2 + nt_1_2 <= 0
 max_tubes_2_3: - 2 x_2_3 + nt_2_3 <= 0
 max_tubes_3_1: - 2 x_3_1 + nt_3_1 <= 0
 max_vehicles_1_2: - nt_1_2 + nv_1_2 <= 0
 max_vehicles_2_3: - nt_2_3 + nv_2_3 <= 0
 max_vehicles_3_1: - nt_3_1 + nv_3_1 <= 0
 max_passengers_1_2: pax_1_2 - 5 nv_1_2 <= 0
 max_passengers_2_3: pax_2_3 - 5 nv_2_3 <= 0
 max_passengers_3_1: pax_3_1 - 5 nv_3_1 <= 0
Bounds
 pax_1_2 <= 5
 pax_2_3 <= 10
 pax_3_1 <= 15
Binaries
 x_1_2 x_2_3 x_3_1
Generals
 pax_1_2 pax_2_3 pax_3_1 nt_1_2 nt_2_3 nt_3_1 nv_1_2 nv_2_3 nv_3_1
End
