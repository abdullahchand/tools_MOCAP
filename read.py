import numpy as np
import json
import tqdm
# import numpy as np
# js = np.load("/Users/macbookpro/Documents/GridgeAI/Movrs/MultiViewSMPL/frame.npz",allow_pickle=True)
# with np.load("/Users/macbookpro/Documents/GridgeAI/Movrs/MultiViewSMPL/frame0006.png_pose.npz_vis.png_pose.npz") as data:
#     a = data
#     print str(list(a['pose']))
with open("/mnt/g/Ubuntu/Movrs/MOCAP/filtered_result.json", "r") as json_file:
    keypoints = json.load(json_file)

keypoints_list = []
count = 0
final_array={}
final_array['pose']=[]
final_array['pose'].append([])
final_array['pose'].append([])
final_array['pose'].append([])
final_array['pose'].append([])
final_array['pose'].append([])

final_array['pose'][0]=[]
final_array['pose'][1]=[]
final_array['pose'][2]=[]
final_array['pose'][3]=[]
final_array['pose'][4]=[]
test2 =[]
total_keypoints = []
count = 0
for i in range(len(keypoints)):
    keypoints[i]["keypoints"] = np.array(keypoints[i]["keypoints"]).reshape(-1,3)
    total_keypoints.append(np.array(keypoints[i]["keypoints"]).reshape(-1,17,3))
print(str(len(keypoints)))
count=len(keypoints)-1
#[]
for i in keypoints:
    # print(str(i['keypoints']))
    X = []
    Y=[]
    Z=[]
    i['keypoints'] = [i['keypoints'][16],i['keypoints'][14],i['keypoints'][12],i['keypoints'][11],i['keypoints'][13],i['keypoints'][15],i['keypoints'][10],i['keypoints'][8],i['keypoints'][6],i['keypoints'][5],i['keypoints'][7],i['keypoints'][9],(i['keypoints'][5]+i['keypoints'][6])/2,i['keypoints'][0]]
    for l in i['keypoints']:
        X.append(l[0])
        Y.append(l[1])
        Z.append(l[2])
    final_array['pose'][0] = X
    final_array['pose'][1] = Y
    final_array['pose'][2] = Z
    print("Final_array"+str(final_array))
    # np.save("/mnt/e/Ubuntu/Movrs/saved2d_pose/frame%04d.jpg_pose.npy" % count,final_array)
    with open("/mnt/g/Ubuntu/Movrs/MultiViewSMPL/saved2d_pose/frame%04d.jpg_pose.json" % count, 'w+') as outfile:
        json.dump(final_array, outfile)
    count-=1
    # other_kps = np.array(other_kp).reshape(-1,3)
    # kps = np.array(i).reshape(-1,3)

    # kps = np.concatenate(kps, axis=0)
    # points = np.vstack( (kps[0], (kps[5] + kps[6])/2, kps[6], kps[8], kps[10], kps[5], kps[7],
    # kps[9],(kps[12] + kps[11])/2, kps[12], kps[14], kps[16], kps[11], kps[13], kps[15], kps[2], kps[1], kps[4], kps[3], [0.0, 0.0,0.0],[0.0, 0.0,0.0],[0.0, 0.0,0.0],[0.0, 0.0,0.0],[0.0, 0.0,0.0],[0.0, 0.0,0.0],[0.0, 0.0,0.0] ))
    # points = [vec for vec in points]
    # points = [np.array(vec) for vec in points]
    # for f in range(len(points)):
    #     test.append(points[f].tolist())
    # # print(str(test))
    #
    # kps = np.array(test).reshape(-1,3)
    # for x in range(len(kps)):
    #     kps[x][2]=keypoints[i]["score"]
    # # kps = np.insert(kps,[9],[(kps[8][0]+kps[11][0])/2,(kps[8][1]+kps[11][1])/2,1.0])
    # print(str(kps))
    # # for x in range(20,25):
    # #     print(kps[x])
    # #     kps = np.append(kps,[0,0,0])
    #
    #
    # # kps = np.append(kps,[0,0,0])
    # # kps = np.append(kps,[0,0,0])
    # # kps = np.append(kps,[0,0,0])
    # # kps = np.append(kps,[0,0,0])
    # # kps = np.append(kps,[0,0,0])
    # # kps = np.append(kps,[0,0,0])
    # # kps = np.append(kps,[0,0,0])
    # kps = kps.reshape(1,-1)
    # kps = np.asarray(kps)
    # kps_converted = convert_kps(kps,src='coco',dst='spin')
    # kps = kps.reshape(1,-1)
    # print("Length : " +str(len(kps.tolist()[0])))
    # print(str(kps.tolist()[0]))
    # data = {}
    # data['version'] = 1.3
    # #
    # data['people'] = []
    # data['people'].append({'person_id':[],'pose_keypoints_2d':kps.tolist()[0],"face_keypoints_2d":[],"hand_left_keypoints_2d":[],"hand_right_keypoints_2d":[],"pose_keypoints_3d":[],"face_keypoints_3d":[],"hand_left_keypoints_3d":[],"hand_right_keypoints_3d":[]})
    # filename = "/Users/macbookpro/Documents/GridgeAI/Movrs/MOCAP-master/3dpose_gan/output/sample_video_%012d_keypoints.json" % count
    # with open(filename, 'w+') as outfile:
    #     json.dump(data, outfile)
    #     count+=1
