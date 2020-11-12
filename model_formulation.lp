\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  2 pax_1_2 + 2 pax_2_3 + 5 pax_3_1 + 3 pax_2_4 + 4 pax_1_4 + 4 pax_3_4
   - 2 x_1_2 - 2 x_2_3 - 4 x_3_1 - 4 x_2_4 - 2 x_1_4 - 2 x_3_4 - 25 nt_1_2
   - 25 nt_2_3 - 25 nt_3_1 - 25 nt_2_4 - 25 nt_1_4 - 25 nt_3_4 - 2 nv_1_2
   - 2 nv_2_3 - 2 nv_3_1 - 2 nv_2_4 - 2 nv_1_4 - 2 nv_3_4
Subject To
 max_tubes_1_2: - 2 x_1_2 + nt_1_2 <= 0
 max_tubes_2_3: - 2 x_2_3 + nt_2_3 <= 0
 max_tubes_3_1: - 2 x_3_1 + nt_3_1 <= 0
 max_tubes_2_4: - 3 x_2_4 + nt_2_4 <= 0
 max_tubes_1_4: - 3 x_1_4 + nt_1_4 <= 0
 max_tubes_3_4: - x_3_4 + nt_3_4 <= 0
 max_vehicles_1_2: - nt_1_2 + nv_1_2 <= 0
 max_vehicles_2_3: - nt_2_3 + nv_2_3 <= 0
 max_vehicles_3_1: - nt_3_1 + nv_3_1 <= 0
 max_vehicles_2_4: - nt_2_4 + nv_2_4 <= 0
 max_vehicles_1_4: - nt_1_4 + nv_1_4 <= 0
 max_vehicles_3_4: - nt_3_4 + nv_3_4 <= 0
 max_passengers_1_2: pax_1_2 - 5 nv_1_2 <= 0
 max_passengers_2_3: pax_2_3 - 5 nv_2_3 <= 0
 max_passengers_3_1: pax_3_1 - 5 nv_3_1 <= 0
 max_passengers_2_4: pax_2_4 - 5 nv_2_4 <= 0
 max_passengers_1_4: pax_1_4 - 5 nv_1_4 <= 0
 max_passengers_3_4: pax_3_4 - 5 nv_3_4 <= 0
 node_connected_1: - x_1_2 - x_3_1 - x_1_4 <= -1
 node_connected_2: - x_1_2 - x_2_3 - x_2_4 <= -1
 node_connected_3: - x_2_3 - x_3_1 - x_3_4 <= -1
 node_connected_4: - x_2_4 - x_1_4 - x_3_4 <= -1
 min_amount_links: x_1_2 + x_2_3 + x_3_1 + x_2_4 + x_1_4 + x_3_4 >= 3
Bounds
 pax_1_2 <= 5
 pax_2_3 <= 10
 pax_3_1 <= 15
 pax_2_4 <= 12
 pax_1_4 <= 13
 pax_3_4 <= 9
Binaries
 x_1_2 x_2_3 x_3_1 x_2_4 x_1_4 x_3_4
Generals
 pax_1_2 pax_2_3 pax_3_1 pax_2_4 pax_1_4 pax_3_4 nt_1_2 nt_2_3 nt_3_1
 nt_2_4 nt_1_4 nt_3_4 nv_1_2 nv_2_3 nv_3_1 nv_2_4 nv_1_4 nv_3_4
End
