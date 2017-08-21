import tensorflow as tf

print("get session")
sess = tf.Session()
with tf.Session() as sess:
    print("import meta graph")
    new_saver = tf.train.import_meta_graph('./11000-cpu/basic-11000.meta')
    print("restore data weights")
    new_saver.restore(sess, './11000-cpu/basic-11000.data-00000-of-00001')
    print("get collection")
    collection = tf.Graph.get_collection(tf.GraphKeys.GLOBAL_VARIABLES) 
    print("print collection")
    print(collection)