Robot Framework 

    1��ͨ���͵��Զ������Կ��
        *��֯�Զ����ű�
        *ѡ����Խű�ִ��(����ִ�л�ָ��ִ��)
        *���Խ���������ķ���ÿ�����Խű��������ű��Ƿ�ͨ��
        *ִ�еĽ�������ײ鿴�ı�����ʽ�ύ�����˲���
        
        *�Զ�����������ʵ������
        *�Զ����������Ŀ���֧��(IDE��ku)
        *����������ϵͳ�ļ���(����)
        *����ִ��--->��ز����׼��Ͳ�������ִ�еĹ���
                    ��ʼ�������
                    ���Ա���
                    
    2���ṹ
            �Զ��������������ļ�
            
            Robot Framework 
                                -------->   ����ϵͳ
            ���Կ�
            
            ���Թ���1  ���Թ���n
            
     *������Ա�������������ļ�(Test Data)��Ӧһ������������
     *���������ļ�����ʹ�õĹ���Сģ���"�ؼ���",�ɲ��Կ�(Test Library)ʵ��
     *Robot Framework���ز��Կ⣬������ִ�в�������
     
    3���ص�
        ��1���Թؼ��ֵ���ʽ��������������
            *��׼���ṩ�˳��õĹ���
            *��������չ��
            *�����߸��ݲ�Ʒ���п�����
                �Զ������Կ�ܡ��⿪����
                �Զ�������������
                
        ��2������������������Ĳ�������ִ�п��ƣ�������ʼ�������������
        ��3����������־�ͱ����ܣ���������Ĳ鿴����ִ�н��
RF�İ�װ

    RF�İ�װ��pip install robotframework
    
    RIDE�İ�װ��һ�㲻�ã�
        *�򵥵�IDE
        *�ṩ��RF�Զ������������Ŀ��ӻ��ı༭���� pip install robotframework-ride
        *wxpython�İ�װ---RIDE����wxpython��ͼ�ο�2.8.12.1
        
    seleniumlibrary�İ�װ
        *֧��selenium�Զ�����RF��չ��
        *pip install --upgrade robotframework-seleniumlibrary
        
        ��װ���ʹ���������ʾ(IntelliBot)
        
    SeleniumLibrary�ĵ���ַ��robotframework.org/SeleniumLibrary/SeleniumLibrary.html
    ��׼����ַ��robotframework.org/#libraries
    
�׼��������ļ����ļ��еı�

    RF֧�����ֵı�
        *�ֱ�ΪSettings, Variables, Test Cases, Keywords
        *������������ڵ�һ����Ԫ���У�������Сд������
        
    һ��Settings������������׼���ȫ�����ñ����磬˵����������׼�Ҫʹ�õĲ��Կ⣬��Դ�ļ�������
    �׼��Ļ�����ʼ����setup���������teardown�������׼��ڵı�ǩ��
    ����Variables��------->�����׼�ȫ�ֱ�����
    ����Test Cases��------>������������׼��Ĳ�������
    �ġ�Keywords��-------->��������׼����û��ؼ���
        
�����������﷨

    ���������������ÿ������������ſ��Է�Ϊ��
        *���ò���
        *���岿��
    �������ò���
        *[Documentation]
        ������������˵��
        *[Tags]
        �������ı�ǩ
        *[Setup],[Teardown]
        �������ĳ�ʼ�����������
        *[Template]
        ������������ģ��ؼ���������
        *[Timeout]
        ����������ʱʱ��
    ���������岿����Ҫ�ɹؼ������
    *�ؼ��ֵ���Դ
        ���Կ�
        ��Դ�ļ�
        �������ڵ��ļ��Ĺؼ��ֱ�
    *���������岿��Ҳ����������ֵ
    
���ùؼ���

    *Import Library
    
    *Should Be Equal
        Should Be Equal  10  010    �������ַ������бȽϣ����Խ����False
        Should Be Equal As Integer  10   010     ��Ͱ���ת�������ֶ�����бȽϣ����ΪTrue
        
    *Should Contain
    
    *set variable
        ${var}   set variable   ${EMPTY}   ���ÿ��ַ���
        
    *log to console  ��ӡ�ڿ���̨
        log to console 32  ��ʾ�ַ�����32��
        log to console ${32}  ��ʾ����32
        
    *log 
    *sleep
    *Convert To Integer  ת�����ַ���
    
    *Convert To Number   ת���ɸ�����
    
    *Should Be True
       ${str1} =  set varuabke  hello
       Should Be True  $str1=='hello'
        
    *eval        ��̬����Ϸ����ʽ
        exp = input('��������ʽ:')
        print(eval(exp))
        