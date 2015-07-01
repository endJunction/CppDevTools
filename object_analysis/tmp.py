get_ipython().magic("run 'symbols.py'")
df = nm('/home/naumov/w/ogs/build/bin/ogs')
count_equal(df)
cost_by_count_and_size(df)
libs = nm('/home/naumov/w/ogs/build/lib/libApplicationsLib.a')
lib_files=['/home/naumov/w/ogs/build/lib/libApplicationsLib.a', '/home/naumov/w/ogs/build/lib/libAssemblerLib.a', '/home/naumov/w/ogs/build/lib/libBaseLib.a', '/home/naumov/w/ogs/build/lib/libFileIO.a', '/home/naumov/w/ogs/build/lib/libGeoLib.a', '/home/naumov/w/ogs/build/lib/libInSituLib.a', '/home/naumov/w/ogs/build/lib/libMathLib.a', '/home/naumov/w/ogs/build/lib/libMeshGeoToolsLib.a', '/home/naumov/w/ogs/build/lib/libMeshLib.a', '/home/naumov/w/ogs/build/lib/libNumLib.a', '/home/naumov/w/ogs/build/lib/libProcessLib.a']

libs = pd.DataFrame()
for f in lib_files:
    if libs.empty:
        libs = nm(f)
    else:
        a = nm(f)
        print(len(libs))
        libs=libs.append(a)
        print(len(libs))
    print(len(a))
    
count_equal(libs)
cost_by_count_and_size(libs)
libs.sort('cost').tail(100)
