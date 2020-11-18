\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  4 pax_1_2 + 3 pax_1_3 + 4 pax_1_4 + 4 pax_1_5 + 8 pax_1_6 + 5 pax_1_7
   + 9 pax_1_8 + 7 pax_2_3 + 4 pax_2_4 + 8 pax_2_5 + 7 pax_2_6 + 6 pax_2_7
   + 7 pax_2_8 + 3 pax_3_4 + 3 pax_3_5 + 2 pax_3_6 + 4 pax_3_7 + 4 pax_3_8
   + 4 pax_4_5 + 5 pax_4_6 + 6 pax_4_7 + 6 pax_4_8 + 9 pax_5_6 + 4 pax_5_7
   + 7 pax_5_8 + 9 pax_6_7 + 8 pax_6_8 + 6 pax_7_8 - 8 x_1_2 - 9 x_1_3
   - 7 x_1_4 - 6 x_1_5 - 6 x_1_6 - 9 x_1_7 - 5 x_1_8 - 9 x_2_3 - 4 x_2_4
   - 5 x_2_5 - 4 x_2_6 - 3 x_2_7 - 7 x_2_8 - 8 x_3_4 - 5 x_3_5 - 8 x_3_6
   - 6 x_3_7 - 7 x_3_8 - 8 x_4_5 - 7 x_4_6 - 8 x_4_7 - 7 x_4_8 - 4 x_5_6
   - 7 x_5_7 - 3 x_5_8 - 9 x_6_7 - 5 x_6_8 - 8 x_7_8 - 50 nt_1_2
   - 50 nt_1_3 - 50 nt_1_4 - 50 nt_1_5 - 50 nt_1_6 - 50 nt_1_7 - 50 nt_1_8
   - 50 nt_2_3 - 50 nt_2_4 - 50 nt_2_5 - 50 nt_2_6 - 50 nt_2_7 - 50 nt_2_8
   - 50 nt_3_4 - 50 nt_3_5 - 50 nt_3_6 - 50 nt_3_7 - 50 nt_3_8 - 50 nt_4_5
   - 50 nt_4_6 - 50 nt_4_7 - 50 nt_4_8 - 50 nt_5_6 - 50 nt_5_7 - 50 nt_5_8
   - 50 nt_6_7 - 50 nt_6_8 - 50 nt_7_8 - 6 nv_1_2 - 6 nv_1_3 - 6 nv_1_4
   - 6 nv_1_5 - 6 nv_1_6 - 6 nv_1_7 - 6 nv_1_8 - 6 nv_2_3 - 6 nv_2_4
   - 6 nv_2_5 - 6 nv_2_6 - 6 nv_2_7 - 6 nv_2_8 - 6 nv_3_4 - 6 nv_3_5
   - 6 nv_3_6 - 6 nv_3_7 - 6 nv_3_8 - 6 nv_4_5 - 6 nv_4_6 - 6 nv_4_7
   - 6 nv_4_8 - 6 nv_5_6 - 6 nv_5_7 - 6 nv_5_8 - 6 nv_6_7 - 6 nv_6_8
   - 6 nv_7_8
Subject To
 max_tubes_1_2: - 6 x_1_2 + nt_1_2 <= 0
 max_tubes_1_3: - 6 x_1_3 + nt_1_3 <= 0
 max_tubes_1_4: - 9 x_1_4 + nt_1_4 <= 0
 max_tubes_1_5: - 4 x_1_5 + nt_1_5 <= 0
 max_tubes_1_6: - 7 x_1_6 + nt_1_6 <= 0
 max_tubes_1_7: - 6 x_1_7 + nt_1_7 <= 0
 max_tubes_1_8: - 7 x_1_8 + nt_1_8 <= 0
 max_tubes_2_3: - 5 x_2_3 + nt_2_3 <= 0
 max_tubes_2_4: - 2 x_2_4 + nt_2_4 <= 0
 max_tubes_2_5: - 5 x_2_5 + nt_2_5 <= 0
 max_tubes_2_6: - 7 x_2_6 + nt_2_6 <= 0
 max_tubes_2_7: - 3 x_2_7 + nt_2_7 <= 0
 max_tubes_2_8: - 2 x_2_8 + nt_2_8 <= 0
 max_tubes_3_4: - 6 x_3_4 + nt_3_4 <= 0
 max_tubes_3_5: - 8 x_3_5 + nt_3_5 <= 0
 max_tubes_3_6: - 8 x_3_6 + nt_3_6 <= 0
 max_tubes_3_7: - 3 x_3_7 + nt_3_7 <= 0
 max_tubes_3_8: - 7 x_3_8 + nt_3_8 <= 0
 max_tubes_4_5: - 6 x_4_5 + nt_4_5 <= 0
 max_tubes_4_6: - 5 x_4_6 + nt_4_6 <= 0
 max_tubes_4_7: - 5 x_4_7 + nt_4_7 <= 0
 max_tubes_4_8: - 3 x_4_8 + nt_4_8 <= 0
 max_tubes_5_6: - 9 x_5_6 + nt_5_6 <= 0
 max_tubes_5_7: - 6 x_5_7 + nt_5_7 <= 0
 max_tubes_5_8: - 6 x_5_8 + nt_5_8 <= 0
 max_tubes_6_7: - 6 x_6_7 + nt_6_7 <= 0
 max_tubes_6_8: - 7 x_6_8 + nt_6_8 <= 0
 max_tubes_7_8: - 4 x_7_8 + nt_7_8 <= 0
 max_vehicles_1_2: - 2 nt_1_2 + nv_1_2 <= 0
 max_vehicles_1_3: - 2 nt_1_3 + nv_1_3 <= 0
 max_vehicles_1_4: - 2 nt_1_4 + nv_1_4 <= 0
 max_vehicles_1_5: - 2 nt_1_5 + nv_1_5 <= 0
 max_vehicles_1_6: - 2 nt_1_6 + nv_1_6 <= 0
 max_vehicles_1_7: - 2 nt_1_7 + nv_1_7 <= 0
 max_vehicles_1_8: - 2 nt_1_8 + nv_1_8 <= 0
 max_vehicles_2_3: - 2 nt_2_3 + nv_2_3 <= 0
 max_vehicles_2_4: - 2 nt_2_4 + nv_2_4 <= 0
 max_vehicles_2_5: - 2 nt_2_5 + nv_2_5 <= 0
 max_vehicles_2_6: - 2 nt_2_6 + nv_2_6 <= 0
 max_vehicles_2_7: - 2 nt_2_7 + nv_2_7 <= 0
 max_vehicles_2_8: - 2 nt_2_8 + nv_2_8 <= 0
 max_vehicles_3_4: - 2 nt_3_4 + nv_3_4 <= 0
 max_vehicles_3_5: - 2 nt_3_5 + nv_3_5 <= 0
 max_vehicles_3_6: - 2 nt_3_6 + nv_3_6 <= 0
 max_vehicles_3_7: - 2 nt_3_7 + nv_3_7 <= 0
 max_vehicles_3_8: - 2 nt_3_8 + nv_3_8 <= 0
 max_vehicles_4_5: - 2 nt_4_5 + nv_4_5 <= 0
 max_vehicles_4_6: - 2 nt_4_6 + nv_4_6 <= 0
 max_vehicles_4_7: - 2 nt_4_7 + nv_4_7 <= 0
 max_vehicles_4_8: - 2 nt_4_8 + nv_4_8 <= 0
 max_vehicles_5_6: - 2 nt_5_6 + nv_5_6 <= 0
 max_vehicles_5_7: - 2 nt_5_7 + nv_5_7 <= 0
 max_vehicles_5_8: - 2 nt_5_8 + nv_5_8 <= 0
 max_vehicles_6_7: - 2 nt_6_7 + nv_6_7 <= 0
 max_vehicles_6_8: - 2 nt_6_8 + nv_6_8 <= 0
 max_vehicles_7_8: - 2 nt_7_8 + nv_7_8 <= 0
 max_passengers_1_2: pax_1_2 - 50 nv_1_2 <= 0
 max_passengers_1_3: pax_1_3 - 50 nv_1_3 <= 0
 max_passengers_1_4: pax_1_4 - 50 nv_1_4 <= 0
 max_passengers_1_5: pax_1_5 - 50 nv_1_5 <= 0
 max_passengers_1_6: pax_1_6 - 50 nv_1_6 <= 0
 max_passengers_1_7: pax_1_7 - 50 nv_1_7 <= 0
 max_passengers_1_8: pax_1_8 - 50 nv_1_8 <= 0
 max_passengers_2_3: pax_2_3 - 50 nv_2_3 <= 0
 max_passengers_2_4: pax_2_4 - 50 nv_2_4 <= 0
 max_passengers_2_5: pax_2_5 - 50 nv_2_5 <= 0
 max_passengers_2_6: pax_2_6 - 50 nv_2_6 <= 0
 max_passengers_2_7: pax_2_7 - 50 nv_2_7 <= 0
 max_passengers_2_8: pax_2_8 - 50 nv_2_8 <= 0
 max_passengers_3_4: pax_3_4 - 50 nv_3_4 <= 0
 max_passengers_3_5: pax_3_5 - 50 nv_3_5 <= 0
 max_passengers_3_6: pax_3_6 - 50 nv_3_6 <= 0
 max_passengers_3_7: pax_3_7 - 50 nv_3_7 <= 0
 max_passengers_3_8: pax_3_8 - 50 nv_3_8 <= 0
 max_passengers_4_5: pax_4_5 - 50 nv_4_5 <= 0
 max_passengers_4_6: pax_4_6 - 50 nv_4_6 <= 0
 max_passengers_4_7: pax_4_7 - 50 nv_4_7 <= 0
 max_passengers_4_8: pax_4_8 - 50 nv_4_8 <= 0
 max_passengers_5_6: pax_5_6 - 50 nv_5_6 <= 0
 max_passengers_5_7: pax_5_7 - 50 nv_5_7 <= 0
 max_passengers_5_8: pax_5_8 - 50 nv_5_8 <= 0
 max_passengers_6_7: pax_6_7 - 50 nv_6_7 <= 0
 max_passengers_6_8: pax_6_8 - 50 nv_6_8 <= 0
 max_passengers_7_8: pax_7_8 - 50 nv_7_8 <= 0
 node_connected_1: - x_1_2 - x_1_3 - x_1_4 - x_1_5 - x_1_6 - x_1_7 - x_1_8
   <= -1
 node_connected_2: - x_1_2 - x_2_3 - x_2_4 - x_2_5 - x_2_6 - x_2_7 - x_2_8
   <= -1
 node_connected_3: - x_1_3 - x_2_3 - x_3_4 - x_3_5 - x_3_6 - x_3_7 - x_3_8
   <= -1
 node_connected_4: - x_1_4 - x_2_4 - x_3_4 - x_4_5 - x_4_6 - x_4_7 - x_4_8
   <= -1
 node_connected_5: - x_1_5 - x_2_5 - x_3_5 - x_4_5 - x_5_6 - x_5_7 - x_5_8
   <= -1
 node_connected_6: - x_1_6 - x_2_6 - x_3_6 - x_4_6 - x_5_6 - x_6_7 - x_6_8
   <= -1
 node_connected_7: - x_1_7 - x_2_7 - x_3_7 - x_4_7 - x_5_7 - x_6_7 - x_7_8
   <= -1
 node_connected_8: - x_1_8 - x_2_8 - x_3_8 - x_4_8 - x_5_8 - x_6_8 - x_7_8
   <= -1
 min_amount_links: x_1_2 + x_1_3 + x_1_4 + x_1_5 + x_1_6 + x_1_7 + x_1_8
   + x_2_3 + x_2_4 + x_2_5 + x_2_6 + x_2_7 + x_2_8 + x_3_4 + x_3_5 + x_3_6
   + x_3_7 + x_3_8 + x_4_5 + x_4_6 + x_4_7 + x_4_8 + x_5_6 + x_5_7 + x_5_8
   + x_6_7 + x_6_8 + x_7_8 = 7
Bounds
 pax_1_2 <= 60
 pax_1_3 <= 180
 pax_1_4 <= 80
 pax_1_5 <= 160
 pax_1_6 <= 20
 pax_1_7 <= 160
 pax_1_8 <= 180
 pax_2_3 <= 100
 pax_2_4 <= 80
 pax_2_5 <= 80
 pax_2_6 <= 160
 pax_2_7 <= 100
 pax_2_8 <= 180
 pax_3_4 <= 160
 pax_3_5 <= 140
 pax_3_6 <= 100
 pax_3_7 <= 60
 pax_3_8 <= 160
 pax_4_5 <= 160
 pax_4_6 <= 160
 pax_4_7 <= 20
 pax_4_8 <= 100
 pax_5_6 <= 40
 pax_5_7 <= 180
 pax_5_8 <= 80
 pax_6_7 <= 40
 pax_6_8 <= 180
 pax_7_8 <= 100
Binaries
 x_1_2 x_1_3 x_1_4 x_1_5 x_1_6 x_1_7 x_1_8 x_2_3 x_2_4 x_2_5 x_2_6 x_2_7
 x_2_8 x_3_4 x_3_5 x_3_6 x_3_7 x_3_8 x_4_5 x_4_6 x_4_7 x_4_8 x_5_6 x_5_7
 x_5_8 x_6_7 x_6_8 x_7_8
Generals
 pax_1_2 pax_1_3 pax_1_4 pax_1_5 pax_1_6 pax_1_7 pax_1_8 pax_2_3 pax_2_4
 pax_2_5 pax_2_6 pax_2_7 pax_2_8 pax_3_4 pax_3_5 pax_3_6 pax_3_7 pax_3_8
 pax_4_5 pax_4_6 pax_4_7 pax_4_8 pax_5_6 pax_5_7 pax_5_8 pax_6_7 pax_6_8
 pax_7_8 nt_1_2 nt_1_3 nt_1_4 nt_1_5 nt_1_6 nt_1_7 nt_1_8 nt_2_3 nt_2_4
 nt_2_5 nt_2_6 nt_2_7 nt_2_8 nt_3_4 nt_3_5 nt_3_6 nt_3_7 nt_3_8 nt_4_5
 nt_4_6 nt_4_7 nt_4_8 nt_5_6 nt_5_7 nt_5_8 nt_6_7 nt_6_8 nt_7_8 nv_1_2
 nv_1_3 nv_1_4 nv_1_5 nv_1_6 nv_1_7 nv_1_8 nv_2_3 nv_2_4 nv_2_5 nv_2_6
 nv_2_7 nv_2_8 nv_3_4 nv_3_5 nv_3_6 nv_3_7 nv_3_8 nv_4_5 nv_4_6 nv_4_7
 nv_4_8 nv_5_6 nv_5_7 nv_5_8 nv_6_7 nv_6_8 nv_7_8
End
