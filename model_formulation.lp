\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  6 pax_1_2 + 6 pax_1_3 + 9 pax_1_4 + 4 pax_1_5 + 7 pax_1_6 + 9 pax_1_7
   + 8 pax_1_8 + 6 pax_1_9 + 8 pax_1_10 + 6 pax_2_3 + 5 pax_2_4 + 5 pax_2_5
   + 8 pax_2_6 + 4 pax_2_7 + 3 pax_2_8 + 4 pax_2_9 + 3 pax_2_10 + 4 pax_3_4
   + 6 pax_3_5 + 7 pax_3_6 + 7 pax_3_7 + 6 pax_3_8 + 6 pax_3_9 + 2 pax_3_10
   + 8 pax_4_5 + 5 pax_4_6 + 8 pax_4_7 + 5 pax_4_8 + 6 pax_4_9 + 2 pax_4_10
   + 7 pax_5_6 + 3 pax_5_7 + 7 pax_5_8 + 4 pax_5_9 + 9 pax_5_10 + 2 pax_6_7
   + 8 pax_6_8 + 5 pax_6_9 + 2 pax_6_10 + 9 pax_7_8 + 5 pax_7_9 + pax_7_10
   + 5 pax_8_9 + 3 pax_8_10 + 6 pax_9_10 - 5 x_1_2 - 2 x_1_3 - 5 x_1_4
   - 7 x_1_5 - 3 x_1_6 - 2 x_1_7 - 6 x_1_8 - 8 x_1_9 - 8 x_1_10 - 3 x_2_3
   - 7 x_2_4 - 6 x_2_5 - 5 x_2_6 - 5 x_2_7 - 3 x_2_8 - 9 x_2_9 - 6 x_2_10
   - 6 x_3_4 - 6 x_3_5 - 7 x_3_6 - 4 x_3_7 - 5 x_3_8 - 8 x_3_9 - 6 x_3_10
   - 3 x_4_5 - 9 x_4_6 - 8 x_4_7 - 6 x_4_8 - 2 x_4_9 - 8 x_4_10 - 9 x_5_6
   - 6 x_5_7 - 4 x_5_8 - 8 x_5_9 - 4 x_5_10 - 2 x_6_7 - 9 x_6_8 - 4 x_6_9
   - 5 x_6_10 - 4 x_7_8 - 9 x_7_9 - 7 x_7_10 - 3 x_8_9 - 9 x_8_10
   - 8 x_9_10 - 150 nt_1_2 - 150 nt_1_3 - 150 nt_1_4 - 150 nt_1_5
   - 150 nt_1_6 - 150 nt_1_7 - 150 nt_1_8 - 150 nt_1_9 - 150 nt_1_10
   - 150 nt_2_3 - 150 nt_2_4 - 150 nt_2_5 - 150 nt_2_6 - 150 nt_2_7
   - 150 nt_2_8 - 150 nt_2_9 - 150 nt_2_10 - 150 nt_3_4 - 150 nt_3_5
   - 150 nt_3_6 - 150 nt_3_7 - 150 nt_3_8 - 150 nt_3_9 - 150 nt_3_10
   - 150 nt_4_5 - 150 nt_4_6 - 150 nt_4_7 - 150 nt_4_8 - 150 nt_4_9
   - 150 nt_4_10 - 150 nt_5_6 - 150 nt_5_7 - 150 nt_5_8 - 150 nt_5_9
   - 150 nt_5_10 - 150 nt_6_7 - 150 nt_6_8 - 150 nt_6_9 - 150 nt_6_10
   - 150 nt_7_8 - 150 nt_7_9 - 150 nt_7_10 - 150 nt_8_9 - 150 nt_8_10
   - 150 nt_9_10 - 9 nv_1_2 - 9 nv_1_3 - 9 nv_1_4 - 9 nv_1_5 - 9 nv_1_6
   - 9 nv_1_7 - 9 nv_1_8 - 9 nv_1_9 - 9 nv_1_10 - 9 nv_2_3 - 9 nv_2_4
   - 9 nv_2_5 - 9 nv_2_6 - 9 nv_2_7 - 9 nv_2_8 - 9 nv_2_9 - 9 nv_2_10
   - 9 nv_3_4 - 9 nv_3_5 - 9 nv_3_6 - 9 nv_3_7 - 9 nv_3_8 - 9 nv_3_9
   - 9 nv_3_10 - 9 nv_4_5 - 9 nv_4_6 - 9 nv_4_7 - 9 nv_4_8 - 9 nv_4_9
   - 9 nv_4_10 - 9 nv_5_6 - 9 nv_5_7 - 9 nv_5_8 - 9 nv_5_9 - 9 nv_5_10
   - 9 nv_6_7 - 9 nv_6_8 - 9 nv_6_9 - 9 nv_6_10 - 9 nv_7_8 - 9 nv_7_9
   - 9 nv_7_10 - 9 nv_8_9 - 9 nv_8_10 - 9 nv_9_10
Subject To
 max_tubes_1_2: - 5 x_1_2 + nt_1_2 <= 0
 max_tubes_1_3: - 3 x_1_3 + nt_1_3 <= 0
 max_tubes_1_4: - 9 x_1_4 + nt_1_4 <= 0
 max_tubes_1_5: - 5 x_1_5 + nt_1_5 <= 0
 max_tubes_1_6: - 2 x_1_6 + nt_1_6 <= 0
 max_tubes_1_7: - 5 x_1_7 + nt_1_7 <= 0
 max_tubes_1_8: - 6 x_1_8 + nt_1_8 <= 0
 max_tubes_1_9: - 9 x_1_9 + nt_1_9 <= 0
 max_tubes_1_10: - 3 x_1_10 + nt_1_10 <= 0
 max_tubes_2_3: - 5 x_2_3 + nt_2_3 <= 0
 max_tubes_2_4: - 4 x_2_4 + nt_2_4 <= 0
 max_tubes_2_5: - 9 x_2_5 + nt_2_5 <= 0
 max_tubes_2_6: - 8 x_2_6 + nt_2_6 <= 0
 max_tubes_2_7: - 7 x_2_7 + nt_2_7 <= 0
 max_tubes_2_8: - 5 x_2_8 + nt_2_8 <= 0
 max_tubes_2_9: - 4 x_2_9 + nt_2_9 <= 0
 max_tubes_2_10: - 8 x_2_10 + nt_2_10 <= 0
 max_tubes_3_4: - 4 x_3_4 + nt_3_4 <= 0
 max_tubes_3_5: - 4 x_3_5 + nt_3_5 <= 0
 max_tubes_3_6: - 3 x_3_6 + nt_3_6 <= 0
 max_tubes_3_7: - 4 x_3_7 + nt_3_7 <= 0
 max_tubes_3_8: - 7 x_3_8 + nt_3_8 <= 0
 max_tubes_3_9: - 3 x_3_9 + nt_3_9 <= 0
 max_tubes_3_10: - 5 x_3_10 + nt_3_10 <= 0
 max_tubes_4_5: - 4 x_4_5 + nt_4_5 <= 0
 max_tubes_4_6: - 5 x_4_6 + nt_4_6 <= 0
 max_tubes_4_7: - 7 x_4_7 + nt_4_7 <= 0
 max_tubes_4_8: - 6 x_4_8 + nt_4_8 <= 0
 max_tubes_4_9: - 4 x_4_9 + nt_4_9 <= 0
 max_tubes_4_10: - 6 x_4_10 + nt_4_10 <= 0
 max_tubes_5_6: - 3 x_5_6 + nt_5_6 <= 0
 max_tubes_5_7: - 9 x_5_7 + nt_5_7 <= 0
 max_tubes_5_8: - 9 x_5_8 + nt_5_8 <= 0
 max_tubes_5_9: - 7 x_5_9 + nt_5_9 <= 0
 max_tubes_5_10: - 5 x_5_10 + nt_5_10 <= 0
 max_tubes_6_7: - 9 x_6_7 + nt_6_7 <= 0
 max_tubes_6_8: - 3 x_6_8 + nt_6_8 <= 0
 max_tubes_6_9: - 7 x_6_9 + nt_6_9 <= 0
 max_tubes_6_10: - 8 x_6_10 + nt_6_10 <= 0
 max_tubes_7_8: - 5 x_7_8 + nt_7_8 <= 0
 max_tubes_7_9: - 2 x_7_9 + nt_7_9 <= 0
 max_tubes_7_10: - 8 x_7_10 + nt_7_10 <= 0
 max_tubes_8_9: - 2 x_8_9 + nt_8_9 <= 0
 max_tubes_8_10: - 8 x_8_10 + nt_8_10 <= 0
 max_tubes_9_10: - 9 x_9_10 + nt_9_10 <= 0
 max_vehicles_1_2: - 2 nt_1_2 + nv_1_2 <= 0
 max_vehicles_1_3: - 2 nt_1_3 + nv_1_3 <= 0
 max_vehicles_1_4: - 2 nt_1_4 + nv_1_4 <= 0
 max_vehicles_1_5: - 2 nt_1_5 + nv_1_5 <= 0
 max_vehicles_1_6: - 2 nt_1_6 + nv_1_6 <= 0
 max_vehicles_1_7: - 2 nt_1_7 + nv_1_7 <= 0
 max_vehicles_1_8: - 2 nt_1_8 + nv_1_8 <= 0
 max_vehicles_1_9: - 2 nt_1_9 + nv_1_9 <= 0
 max_vehicles_1_10: - 2 nt_1_10 + nv_1_10 <= 0
 max_vehicles_2_3: - 2 nt_2_3 + nv_2_3 <= 0
 max_vehicles_2_4: - 2 nt_2_4 + nv_2_4 <= 0
 max_vehicles_2_5: - 2 nt_2_5 + nv_2_5 <= 0
 max_vehicles_2_6: - 2 nt_2_6 + nv_2_6 <= 0
 max_vehicles_2_7: - 2 nt_2_7 + nv_2_7 <= 0
 max_vehicles_2_8: - 2 nt_2_8 + nv_2_8 <= 0
 max_vehicles_2_9: - 2 nt_2_9 + nv_2_9 <= 0
 max_vehicles_2_10: - 2 nt_2_10 + nv_2_10 <= 0
 max_vehicles_3_4: - 2 nt_3_4 + nv_3_4 <= 0
 max_vehicles_3_5: - 2 nt_3_5 + nv_3_5 <= 0
 max_vehicles_3_6: - 2 nt_3_6 + nv_3_6 <= 0
 max_vehicles_3_7: - 2 nt_3_7 + nv_3_7 <= 0
 max_vehicles_3_8: - 2 nt_3_8 + nv_3_8 <= 0
 max_vehicles_3_9: - 2 nt_3_9 + nv_3_9 <= 0
 max_vehicles_3_10: - 2 nt_3_10 + nv_3_10 <= 0
 max_vehicles_4_5: - 2 nt_4_5 + nv_4_5 <= 0
 max_vehicles_4_6: - 2 nt_4_6 + nv_4_6 <= 0
 max_vehicles_4_7: - 2 nt_4_7 + nv_4_7 <= 0
 max_vehicles_4_8: - 2 nt_4_8 + nv_4_8 <= 0
 max_vehicles_4_9: - 2 nt_4_9 + nv_4_9 <= 0
 max_vehicles_4_10: - 2 nt_4_10 + nv_4_10 <= 0
 max_vehicles_5_6: - 2 nt_5_6 + nv_5_6 <= 0
 max_vehicles_5_7: - 2 nt_5_7 + nv_5_7 <= 0
 max_vehicles_5_8: - 2 nt_5_8 + nv_5_8 <= 0
 max_vehicles_5_9: - 2 nt_5_9 + nv_5_9 <= 0
 max_vehicles_5_10: - 2 nt_5_10 + nv_5_10 <= 0
 max_vehicles_6_7: - 2 nt_6_7 + nv_6_7 <= 0
 max_vehicles_6_8: - 2 nt_6_8 + nv_6_8 <= 0
 max_vehicles_6_9: - 2 nt_6_9 + nv_6_9 <= 0
 max_vehicles_6_10: - 2 nt_6_10 + nv_6_10 <= 0
 max_vehicles_7_8: - 2 nt_7_8 + nv_7_8 <= 0
 max_vehicles_7_9: - 2 nt_7_9 + nv_7_9 <= 0
 max_vehicles_7_10: - 2 nt_7_10 + nv_7_10 <= 0
 max_vehicles_8_9: - 2 nt_8_9 + nv_8_9 <= 0
 max_vehicles_8_10: - 2 nt_8_10 + nv_8_10 <= 0
 max_vehicles_9_10: - 2 nt_9_10 + nv_9_10 <= 0
 max_passengers_1_2: pax_1_2 - 6 nv_1_2 <= 0
 max_passengers_1_3: pax_1_3 - 6 nv_1_3 <= 0
 max_passengers_1_4: pax_1_4 - 6 nv_1_4 <= 0
 max_passengers_1_5: pax_1_5 - 6 nv_1_5 <= 0
 max_passengers_1_6: pax_1_6 - 6 nv_1_6 <= 0
 max_passengers_1_7: pax_1_7 - 6 nv_1_7 <= 0
 max_passengers_1_8: pax_1_8 - 6 nv_1_8 <= 0
 max_passengers_1_9: pax_1_9 - 6 nv_1_9 <= 0
 max_passengers_1_10: pax_1_10 - 6 nv_1_10 <= 0
 max_passengers_2_3: pax_2_3 - 6 nv_2_3 <= 0
 max_passengers_2_4: pax_2_4 - 6 nv_2_4 <= 0
 max_passengers_2_5: pax_2_5 - 6 nv_2_5 <= 0
 max_passengers_2_6: pax_2_6 - 6 nv_2_6 <= 0
 max_passengers_2_7: pax_2_7 - 6 nv_2_7 <= 0
 max_passengers_2_8: pax_2_8 - 6 nv_2_8 <= 0
 max_passengers_2_9: pax_2_9 - 6 nv_2_9 <= 0
 max_passengers_2_10: pax_2_10 - 6 nv_2_10 <= 0
 max_passengers_3_4: pax_3_4 - 6 nv_3_4 <= 0
 max_passengers_3_5: pax_3_5 - 6 nv_3_5 <= 0
 max_passengers_3_6: pax_3_6 - 6 nv_3_6 <= 0
 max_passengers_3_7: pax_3_7 - 6 nv_3_7 <= 0
 max_passengers_3_8: pax_3_8 - 6 nv_3_8 <= 0
 max_passengers_3_9: pax_3_9 - 6 nv_3_9 <= 0
 max_passengers_3_10: pax_3_10 - 6 nv_3_10 <= 0
 max_passengers_4_5: pax_4_5 - 6 nv_4_5 <= 0
 max_passengers_4_6: pax_4_6 - 6 nv_4_6 <= 0
 max_passengers_4_7: pax_4_7 - 6 nv_4_7 <= 0
 max_passengers_4_8: pax_4_8 - 6 nv_4_8 <= 0
 max_passengers_4_9: pax_4_9 - 6 nv_4_9 <= 0
 max_passengers_4_10: pax_4_10 - 6 nv_4_10 <= 0
 max_passengers_5_6: pax_5_6 - 6 nv_5_6 <= 0
 max_passengers_5_7: pax_5_7 - 6 nv_5_7 <= 0
 max_passengers_5_8: pax_5_8 - 6 nv_5_8 <= 0
 max_passengers_5_9: pax_5_9 - 6 nv_5_9 <= 0
 max_passengers_5_10: pax_5_10 - 6 nv_5_10 <= 0
 max_passengers_6_7: pax_6_7 - 6 nv_6_7 <= 0
 max_passengers_6_8: pax_6_8 - 6 nv_6_8 <= 0
 max_passengers_6_9: pax_6_9 - 6 nv_6_9 <= 0
 max_passengers_6_10: pax_6_10 - 6 nv_6_10 <= 0
 max_passengers_7_8: pax_7_8 - 6 nv_7_8 <= 0
 max_passengers_7_9: pax_7_9 - 6 nv_7_9 <= 0
 max_passengers_7_10: pax_7_10 - 6 nv_7_10 <= 0
 max_passengers_8_9: pax_8_9 - 6 nv_8_9 <= 0
 max_passengers_8_10: pax_8_10 - 6 nv_8_10 <= 0
 max_passengers_9_10: pax_9_10 - 6 nv_9_10 <= 0
 node_connected_1: - x_1_2 - x_1_3 - x_1_4 - x_1_5 - x_1_6 - x_1_7 - x_1_8
   - x_1_9 - x_1_10 <= -1
 node_connected_2: - x_1_2 - x_2_3 - x_2_4 - x_2_5 - x_2_6 - x_2_7 - x_2_8
   - x_2_9 - x_2_10 <= -1
 node_connected_3: - x_1_3 - x_2_3 - x_3_4 - x_3_5 - x_3_6 - x_3_7 - x_3_8
   - x_3_9 - x_3_10 <= -1
 node_connected_4: - x_1_4 - x_2_4 - x_3_4 - x_4_5 - x_4_6 - x_4_7 - x_4_8
   - x_4_9 - x_4_10 <= -1
 node_connected_5: - x_1_5 - x_2_5 - x_3_5 - x_4_5 - x_5_6 - x_5_7 - x_5_8
   - x_5_9 - x_5_10 <= -1
 node_connected_6: - x_1_6 - x_2_6 - x_3_6 - x_4_6 - x_5_6 - x_6_7 - x_6_8
   - x_6_9 - x_6_10 <= -1
 node_connected_7: - x_1_7 - x_2_7 - x_3_7 - x_4_7 - x_5_7 - x_6_7 - x_7_8
   - x_7_9 - x_7_10 <= -1
 node_connected_8: - x_1_8 - x_2_8 - x_3_8 - x_4_8 - x_5_8 - x_6_8 - x_7_8
   - x_8_9 - x_8_10 <= -1
 node_connected_9: - x_1_9 - x_2_9 - x_3_9 - x_4_9 - x_5_9 - x_6_9 - x_7_9
   - x_8_9 - x_9_10 <= -1
 node_connected_10: - x_1_10 - x_2_10 - x_3_10 - x_4_10 - x_5_10 - x_6_10
   - x_7_10 - x_8_10 - x_9_10 <= -1
 min_amount_links: x_1_2 + x_1_3 + x_1_4 + x_1_5 + x_1_6 + x_1_7 + x_1_8
   + x_1_9 + x_1_10 + x_2_3 + x_2_4 + x_2_5 + x_2_6 + x_2_7 + x_2_8 + x_2_9
   + x_2_10 + x_3_4 + x_3_5 + x_3_6 + x_3_7 + x_3_8 + x_3_9 + x_3_10
   + x_4_5 + x_4_6 + x_4_7 + x_4_8 + x_4_9 + x_4_10 + x_5_6 + x_5_7 + x_5_8
   + x_5_9 + x_5_10 + x_6_7 + x_6_8 + x_6_9 + x_6_10 + x_7_8 + x_7_9
   + x_7_10 + x_8_9 + x_8_10 + x_9_10 >= 9
Bounds
 pax_1_2 <= 160
 pax_1_3 <= 20
 pax_1_4 <= 160
 pax_1_5 <= 180
 pax_1_6 <= 100
 pax_1_7 <= 80
 pax_1_8 <= 80
 pax_1_9 <= 160
 pax_1_10 <= 100
 pax_2_3 <= 180
 pax_2_4 <= 160
 pax_2_5 <= 140
 pax_2_6 <= 100
 pax_2_7 <= 60
 pax_2_8 <= 160
 pax_2_9 <= 160
 pax_2_10 <= 160
 pax_3_4 <= 20
 pax_3_5 <= 100
 pax_3_6 <= 40
 pax_3_7 <= 180
 pax_3_8 <= 80
 pax_3_9 <= 40
 pax_3_10 <= 180
 pax_4_5 <= 100
 pax_4_6 <= 80
 pax_4_7 <= 60
 pax_4_8 <= 80
 pax_4_9 <= 80
 pax_4_10 <= 160
 pax_5_6 <= 100
 pax_5_7 <= 180
 pax_5_8 <= 140
 pax_5_9 <= 80
 pax_5_10 <= 160
 pax_6_7 <= 140
 pax_6_8 <= 120
 pax_6_9 <= 140
 pax_6_10 <= 60
 pax_7_8 <= 60
 pax_7_9 <= 40
 pax_7_10 <= 80
 pax_8_9 <= 80
 pax_8_10 <= 80
 pax_9_10 <= 100
Binaries
 x_1_2 x_1_3 x_1_4 x_1_5 x_1_6 x_1_7 x_1_8 x_1_9 x_1_10 x_2_3 x_2_4 x_2_5
 x_2_6 x_2_7 x_2_8 x_2_9 x_2_10 x_3_4 x_3_5 x_3_6 x_3_7 x_3_8 x_3_9 x_3_10
 x_4_5 x_4_6 x_4_7 x_4_8 x_4_9 x_4_10 x_5_6 x_5_7 x_5_8 x_5_9 x_5_10 x_6_7
 x_6_8 x_6_9 x_6_10 x_7_8 x_7_9 x_7_10 x_8_9 x_8_10 x_9_10
Generals
 pax_1_2 pax_1_3 pax_1_4 pax_1_5 pax_1_6 pax_1_7 pax_1_8 pax_1_9 pax_1_10
 pax_2_3 pax_2_4 pax_2_5 pax_2_6 pax_2_7 pax_2_8 pax_2_9 pax_2_10 pax_3_4
 pax_3_5 pax_3_6 pax_3_7 pax_3_8 pax_3_9 pax_3_10 pax_4_5 pax_4_6 pax_4_7
 pax_4_8 pax_4_9 pax_4_10 pax_5_6 pax_5_7 pax_5_8 pax_5_9 pax_5_10 pax_6_7
 pax_6_8 pax_6_9 pax_6_10 pax_7_8 pax_7_9 pax_7_10 pax_8_9 pax_8_10
 pax_9_10 nt_1_2 nt_1_3 nt_1_4 nt_1_5 nt_1_6 nt_1_7 nt_1_8 nt_1_9 nt_1_10
 nt_2_3 nt_2_4 nt_2_5 nt_2_6 nt_2_7 nt_2_8 nt_2_9 nt_2_10 nt_3_4 nt_3_5
 nt_3_6 nt_3_7 nt_3_8 nt_3_9 nt_3_10 nt_4_5 nt_4_6 nt_4_7 nt_4_8 nt_4_9
 nt_4_10 nt_5_6 nt_5_7 nt_5_8 nt_5_9 nt_5_10 nt_6_7 nt_6_8 nt_6_9 nt_6_10
 nt_7_8 nt_7_9 nt_7_10 nt_8_9 nt_8_10 nt_9_10 nv_1_2 nv_1_3 nv_1_4 nv_1_5
 nv_1_6 nv_1_7 nv_1_8 nv_1_9 nv_1_10 nv_2_3 nv_2_4 nv_2_5 nv_2_6 nv_2_7
 nv_2_8 nv_2_9 nv_2_10 nv_3_4 nv_3_5 nv_3_6 nv_3_7 nv_3_8 nv_3_9 nv_3_10
 nv_4_5 nv_4_6 nv_4_7 nv_4_8 nv_4_9 nv_4_10 nv_5_6 nv_5_7 nv_5_8 nv_5_9
 nv_5_10 nv_6_7 nv_6_8 nv_6_9 nv_6_10 nv_7_8 nv_7_9 nv_7_10 nv_8_9 nv_8_10
 nv_9_10
End
